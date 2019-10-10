static int bfs_add_entry(struct inode *dir, const struct qstr *child, int ino)
{
	const unsigned char *name = child->name;
	int namelen = child->len;
	struct buffer_head *bh;
	struct bfs_dirent *de;
	int block, sblock, eblock, off, pos;
	int i;

	dprintf("name=%s, namelen=%d\n", name, namelen);

	if (!namelen)
		return -ENOENT;
	if (namelen > BFS_NAMELEN)
		return -ENAMETOOLONG;

	sblock = BFS_I(dir)->i_sblock;
	eblock = BFS_I(dir)->i_eblock;
	for (block = sblock; block <= eblock; block++) {
		bh = sb_bread(dir->i_sb, block);
		if (!bh)
			return -EIO;
		for (off = 0; off < BFS_BSIZE; off += BFS_DIRENT_SIZE) {
			de = (struct bfs_dirent *)(bh->b_data + off);
			if (!de->ino) {
				pos = (block - sblock) * BFS_BSIZE + off;
				if (pos >= dir->i_size) {
					dir->i_size += BFS_DIRENT_SIZE;
					dir->i_ctime = current_time(dir);
				}
				dir->i_mtime = current_time(dir);
				mark_inode_dirty(dir);
				de->ino = cpu_to_le16((u16)ino);
				for (i = 0; i < BFS_NAMELEN; i++)
					de->name[i] =
						(i < namelen) ? name[i] : 0;
				mark_buffer_dirty_inode(bh, dir);
				brelse(bh);
				return 0;
			}
		}
		brelse(bh);
	}
	return -ENOSPC;
}

static inline int bfs_namecmp(int len, const unsigned char *name,
							const char *buffer)
{
	if ((len < BFS_NAMELEN) && buffer[len])
		return 0;
	return !memcmp(name, buffer, len);
}

static struct buffer_head *bfs_find_entry(struct inode *dir,
			const struct qstr *child,
			struct bfs_dirent **res_dir)
{
	unsigned long block = 0, offset = 0;
	struct buffer_head *bh = NULL;
	struct bfs_dirent *de;
	const unsigned char *name = child->name;
	int namelen = child->len;

	*res_dir = NULL;
	if (namelen > BFS_NAMELEN)
		return NULL;

	while (block * BFS_BSIZE + offset < dir->i_size) {
		if (!bh) {
			bh = sb_bread(dir->i_sb, BFS_I(dir)->i_sblock + block);
			if (!bh) {
				block++;
				continue;
			}
		}
		de = (struct bfs_dirent *)(bh->b_data + offset);
		offset += BFS_DIRENT_SIZE;
		if (le16_to_cpu(de->ino) &&
				bfs_namecmp(namelen, name, de->name)) {
			*res_dir = de;
			return bh;
		}
		if (offset < bh->b_size)
			continue;
		brelse(bh);
		bh = NULL;
		offset = 0;
		block++;
	}
	brelse(bh);
	return NULL;
}