# Generated from C:/Users/Sergey/PycharmProjects/c-syntax-analyzer/src\Clang.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2^")
        buf.write("\u0414\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,")
        buf.write("\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?")
        buf.write("\3?\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3")
        buf.write("E\3F\3F\3F\3F\3G\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3")
        buf.write("K\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3O\3O\3O\3O\3P\3P\3P\7")
        buf.write("P\u0246\nP\fP\16P\u0249\13P\3Q\3Q\5Q\u024d\nQ\3R\3R\3")
        buf.write("S\3S\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\5T\u025d\nT\3U\3U\3")
        buf.write("U\3U\3U\3V\3V\3V\5V\u0267\nV\3W\3W\5W\u026b\nW\3W\3W\5")
        buf.write("W\u026f\nW\3W\3W\5W\u0273\nW\3W\5W\u0276\nW\3X\3X\3X\6")
        buf.write("X\u027b\nX\rX\16X\u027c\3Y\3Y\7Y\u0281\nY\fY\16Y\u0284")
        buf.write("\13Y\3Z\3Z\7Z\u0288\nZ\fZ\16Z\u028b\13Z\3[\3[\6[\u028f")
        buf.write("\n[\r[\16[\u0290\3\\\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\5")
        buf.write("`\u029e\n`\3`\3`\3`\3`\3`\5`\u02a5\n`\3`\3`\5`\u02a9\n")
        buf.write("`\5`\u02ab\n`\3a\3a\3b\3b\3c\3c\3c\3c\5c\u02b5\nc\3d\3")
        buf.write("d\5d\u02b9\nd\3e\3e\5e\u02bd\ne\3e\5e\u02c0\ne\3e\3e\3")
        buf.write("e\5e\u02c5\ne\5e\u02c7\ne\3f\3f\3f\3f\5f\u02cd\nf\3f\3")
        buf.write("f\3f\3f\5f\u02d3\nf\5f\u02d5\nf\3g\5g\u02d8\ng\3g\3g\3")
        buf.write("g\3g\3g\3g\5g\u02e0\ng\3h\3h\5h\u02e4\nh\3h\3h\3h\5h\u02e9")
        buf.write("\nh\3h\5h\u02ec\nh\3i\3i\3j\6j\u02f1\nj\rj\16j\u02f2\3")
        buf.write("k\5k\u02f6\nk\3k\3k\3k\3k\3k\3k\5k\u02fe\nk\3l\3l\5l\u0302")
        buf.write("\nl\3l\3l\3l\5l\u0307\nl\3l\5l\u030a\nl\3m\6m\u030d\n")
        buf.write("m\rm\16m\u030e\3n\3n\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o")
        buf.write("\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\5o\u0329\no\3p\6p\u032c")
        buf.write("\np\rp\16p\u032d\3q\3q\5q\u0332\nq\3r\3r\3r\3r\5r\u0338")
        buf.write("\nr\3s\3s\3s\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\5t\u0348")
        buf.write("\nt\3u\3u\3u\3u\6u\u034e\nu\ru\16u\u034f\3v\5v\u0353\n")
        buf.write("v\3v\3v\5v\u0357\nv\3v\3v\3w\3w\3w\5w\u035e\nw\3x\6x\u0361")
        buf.write("\nx\rx\16x\u0362\3y\3y\3y\3y\3y\3y\3y\5y\u036c\ny\3z\3")
        buf.write("z\5z\u0370\nz\3z\3z\3z\3z\3z\3z\3z\3z\7z\u037a\nz\fz\16")
        buf.write("z\u037d\13z\3z\3z\3{\3{\3{\3{\3{\7{\u0386\n{\f{\16{\u0389")
        buf.write("\13{\3{\3{\7{\u038d\n{\f{\16{\u0390\13{\3{\3{\3{\3{\3")
        buf.write("|\3|\3|\3|\3|\3|\3|\7|\u039d\n|\f|\16|\u03a0\13|\3|\7")
        buf.write("|\u03a3\n|\f|\16|\u03a6\13|\3|\3|\3}\3}\5}\u03ac\n}\3")
        buf.write("}\3}\5}\u03b0\n}\3}\3}\7}\u03b4\n}\f}\16}\u03b7\13}\3")
        buf.write("}\3}\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3")
        buf.write("~\3~\3~\5~\u03ce\n~\3~\7~\u03d1\n~\f~\16~\u03d4\13~\3")
        buf.write("~\3~\3\177\3\177\5\177\u03da\n\177\3\177\3\177\3\177\3")
        buf.write("\177\3\177\3\177\3\177\3\177\3\177\7\177\u03e5\n\177\f")
        buf.write("\177\16\177\u03e8\13\177\3\177\3\177\3\u0080\6\u0080\u03ed")
        buf.write("\n\u0080\r\u0080\16\u0080\u03ee\3\u0080\3\u0080\3\u0081")
        buf.write("\3\u0081\5\u0081\u03f5\n\u0081\3\u0081\5\u0081\u03f8\n")
        buf.write("\u0081\3\u0081\3\u0081\3\u0082\3\u0082\3\u0082\3\u0082")
        buf.write("\7\u0082\u0400\n\u0082\f\u0082\16\u0082\u0403\13\u0082")
        buf.write("\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write("\3\u0083\3\u0083\7\u0083\u040e\n\u0083\f\u0083\16\u0083")
        buf.write("\u0411\13\u0083\3\u0083\3\u0083\3\u0401\2\u0084\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>")
        buf.write("{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d")
        buf.write("H\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009d")
        buf.write("P\u009fQ\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab")
        buf.write("R\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9")
        buf.write("\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7")
        buf.write("\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1\2\u00d3S\u00d5")
        buf.write("\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3")
        buf.write("\2\u00e5\2\u00e7\2\u00e9\2\u00ebT\u00ed\2\u00ef\2\u00f1")
        buf.write("\2\u00f3U\u00f5V\u00f7W\u00f9X\u00fbY\u00fdZ\u00ff[\u0101")
        buf.write("\\\u0103]\u0105^\3\2\27\5\2C\\aac|\3\2\62;\4\2DDdd\3\2")
        buf.write("\62\63\4\2ZZzz\3\2\63;\3\2\629\5\2\62;CHch\4\2WWww\4\2")
        buf.write("NNnn\4\2--//\6\2HHNNhhnn\6\2\f\f\17\17))^^\f\2$$))AA^")
        buf.write("^cdhhppttvvxx\5\2NNWWww\6\2\f\f\17\17$$^^\3\2%%\3\2}}")
        buf.write("\3\2\177\177\4\2\f\f\17\17\4\2\13\13\"\"\2\u043e\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00d3\3\2\2\2\2\u00eb\3\2\2")
        buf.write("\2\2\u00f3\3\2\2\2\2\u00f5\3\2\2\2\2\u00f7\3\2\2\2\2\u00f9")
        buf.write("\3\2\2\2\2\u00fb\3\2\2\2\2\u00fd\3\2\2\2\2\u00ff\3\2\2")
        buf.write("\2\2\u0101\3\2\2\2\2\u0103\3\2\2\2\2\u0105\3\2\2\2\3\u0107")
        buf.write("\3\2\2\2\5\u010c\3\2\2\2\7\u0112\3\2\2\2\t\u0117\3\2\2")
        buf.write("\2\13\u011c\3\2\2\2\r\u0122\3\2\2\2\17\u012b\3\2\2\2\21")
        buf.write("\u0133\3\2\2\2\23\u0136\3\2\2\2\25\u013d\3\2\2\2\27\u0142")
        buf.write("\3\2\2\2\31\u0147\3\2\2\2\33\u014d\3\2\2\2\35\u0151\3")
        buf.write("\2\2\2\37\u0156\3\2\2\2!\u0159\3\2\2\2#\u0160\3\2\2\2")
        buf.write("%\u0164\3\2\2\2\'\u0169\3\2\2\2)\u0172\3\2\2\2+\u0179")
        buf.write("\3\2\2\2-\u017f\3\2\2\2/\u0186\3\2\2\2\61\u018d\3\2\2")
        buf.write("\2\63\u0194\3\2\2\2\65\u019b\3\2\2\2\67\u01a2\3\2\2\2")
        buf.write("9\u01aa\3\2\2\2;\u01b0\3\2\2\2=\u01b9\3\2\2\2?\u01be\3")
        buf.write("\2\2\2A\u01c7\3\2\2\2C\u01cd\3\2\2\2E\u01cf\3\2\2\2G\u01d1")
        buf.write("\3\2\2\2I\u01d3\3\2\2\2K\u01d5\3\2\2\2M\u01d7\3\2\2\2")
        buf.write("O\u01d9\3\2\2\2Q\u01db\3\2\2\2S\u01de\3\2\2\2U\u01e0\3")
        buf.write("\2\2\2W\u01e3\3\2\2\2Y\u01e6\3\2\2\2[\u01e9\3\2\2\2]\u01eb")
        buf.write("\3\2\2\2_\u01ee\3\2\2\2a\u01f0\3\2\2\2c\u01f3\3\2\2\2")
        buf.write("e\u01f5\3\2\2\2g\u01f7\3\2\2\2i\u01f9\3\2\2\2k\u01fb\3")
        buf.write("\2\2\2m\u01fd\3\2\2\2o\u0200\3\2\2\2q\u0203\3\2\2\2s\u0205")
        buf.write("\3\2\2\2u\u0207\3\2\2\2w\u0209\3\2\2\2y\u020b\3\2\2\2")
        buf.write("{\u020d\3\2\2\2}\u020f\3\2\2\2\177\u0211\3\2\2\2\u0081")
        buf.write("\u0213\3\2\2\2\u0083\u0216\3\2\2\2\u0085\u0219\3\2\2\2")
        buf.write("\u0087\u021c\3\2\2\2\u0089\u021f\3\2\2\2\u008b\u0222\3")
        buf.write("\2\2\2\u008d\u0226\3\2\2\2\u008f\u022a\3\2\2\2\u0091\u022d")
        buf.write("\3\2\2\2\u0093\u0230\3\2\2\2\u0095\u0233\3\2\2\2\u0097")
        buf.write("\u0236\3\2\2\2\u0099\u0239\3\2\2\2\u009b\u023c\3\2\2\2")
        buf.write("\u009d\u023e\3\2\2\2\u009f\u0242\3\2\2\2\u00a1\u024c\3")
        buf.write("\2\2\2\u00a3\u024e\3\2\2\2\u00a5\u0250\3\2\2\2\u00a7\u025c")
        buf.write("\3\2\2\2\u00a9\u025e\3\2\2\2\u00ab\u0266\3\2\2\2\u00ad")
        buf.write("\u0275\3\2\2\2\u00af\u0277\3\2\2\2\u00b1\u027e\3\2\2\2")
        buf.write("\u00b3\u0285\3\2\2\2\u00b5\u028c\3\2\2\2\u00b7\u0292\3")
        buf.write("\2\2\2\u00b9\u0295\3\2\2\2\u00bb\u0297\3\2\2\2\u00bd\u0299")
        buf.write("\3\2\2\2\u00bf\u02aa\3\2\2\2\u00c1\u02ac\3\2\2\2\u00c3")
        buf.write("\u02ae\3\2\2\2\u00c5\u02b4\3\2\2\2\u00c7\u02b8\3\2\2\2")
        buf.write("\u00c9\u02c6\3\2\2\2\u00cb\u02d4\3\2\2\2\u00cd\u02df\3")
        buf.write("\2\2\2\u00cf\u02eb\3\2\2\2\u00d1\u02ed\3\2\2\2\u00d3\u02f0")
        buf.write("\3\2\2\2\u00d5\u02fd\3\2\2\2\u00d7\u0309\3\2\2\2\u00d9")
        buf.write("\u030c\3\2\2\2\u00db\u0310\3\2\2\2\u00dd\u0328\3\2\2\2")
        buf.write("\u00df\u032b\3\2\2\2\u00e1\u0331\3\2\2\2\u00e3\u0337\3")
        buf.write("\2\2\2\u00e5\u0339\3\2\2\2\u00e7\u0347\3\2\2\2\u00e9\u0349")
        buf.write("\3\2\2\2\u00eb\u0352\3\2\2\2\u00ed\u035d\3\2\2\2\u00ef")
        buf.write("\u0360\3\2\2\2\u00f1\u036b\3\2\2\2\u00f3\u036d\3\2\2\2")
        buf.write("\u00f5\u0380\3\2\2\2\u00f7\u0395\3\2\2\2\u00f9\u03a9\3")
        buf.write("\2\2\2\u00fb\u03ba\3\2\2\2\u00fd\u03d7\3\2\2\2\u00ff\u03ec")
        buf.write("\3\2\2\2\u0101\u03f7\3\2\2\2\u0103\u03fb\3\2\2\2\u0105")
        buf.write("\u0409\3\2\2\2\u0107\u0108\7c\2\2\u0108\u0109\7w\2\2\u0109")
        buf.write("\u010a\7v\2\2\u010a\u010b\7q\2\2\u010b\4\3\2\2\2\u010c")
        buf.write("\u010d\7d\2\2\u010d\u010e\7t\2\2\u010e\u010f\7g\2\2\u010f")
        buf.write("\u0110\7c\2\2\u0110\u0111\7m\2\2\u0111\6\3\2\2\2\u0112")
        buf.write("\u0113\7e\2\2\u0113\u0114\7c\2\2\u0114\u0115\7u\2\2\u0115")
        buf.write("\u0116\7g\2\2\u0116\b\3\2\2\2\u0117\u0118\7e\2\2\u0118")
        buf.write("\u0119\7j\2\2\u0119\u011a\7c\2\2\u011a\u011b\7t\2\2\u011b")
        buf.write("\n\3\2\2\2\u011c\u011d\7e\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write("\u011f\7p\2\2\u011f\u0120\7u\2\2\u0120\u0121\7v\2\2\u0121")
        buf.write("\f\3\2\2\2\u0122\u0123\7e\2\2\u0123\u0124\7q\2\2\u0124")
        buf.write("\u0125\7p\2\2\u0125\u0126\7v\2\2\u0126\u0127\7k\2\2\u0127")
        buf.write("\u0128\7p\2\2\u0128\u0129\7w\2\2\u0129\u012a\7g\2\2\u012a")
        buf.write("\16\3\2\2\2\u012b\u012c\7f\2\2\u012c\u012d\7g\2\2\u012d")
        buf.write("\u012e\7h\2\2\u012e\u012f\7c\2\2\u012f\u0130\7w\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131\u0132\7v\2\2\u0132\20\3\2\2\2\u0133")
        buf.write("\u0134\7f\2\2\u0134\u0135\7q\2\2\u0135\22\3\2\2\2\u0136")
        buf.write("\u0137\7f\2\2\u0137\u0138\7q\2\2\u0138\u0139\7w\2\2\u0139")
        buf.write("\u013a\7d\2\2\u013a\u013b\7n\2\2\u013b\u013c\7g\2\2\u013c")
        buf.write("\24\3\2\2\2\u013d\u013e\7g\2\2\u013e\u013f\7n\2\2\u013f")
        buf.write("\u0140\7u\2\2\u0140\u0141\7g\2\2\u0141\26\3\2\2\2\u0142")
        buf.write("\u0143\7g\2\2\u0143\u0144\7p\2\2\u0144\u0145\7w\2\2\u0145")
        buf.write("\u0146\7o\2\2\u0146\30\3\2\2\2\u0147\u0148\7h\2\2\u0148")
        buf.write("\u0149\7n\2\2\u0149\u014a\7q\2\2\u014a\u014b\7c\2\2\u014b")
        buf.write("\u014c\7v\2\2\u014c\32\3\2\2\2\u014d\u014e\7h\2\2\u014e")
        buf.write("\u014f\7q\2\2\u014f\u0150\7t\2\2\u0150\34\3\2\2\2\u0151")
        buf.write("\u0152\7i\2\2\u0152\u0153\7q\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write("\u0155\7q\2\2\u0155\36\3\2\2\2\u0156\u0157\7k\2\2\u0157")
        buf.write("\u0158\7h\2\2\u0158 \3\2\2\2\u0159\u015a\7k\2\2\u015a")
        buf.write("\u015b\7p\2\2\u015b\u015c\7n\2\2\u015c\u015d\7k\2\2\u015d")
        buf.write("\u015e\7p\2\2\u015e\u015f\7g\2\2\u015f\"\3\2\2\2\u0160")
        buf.write("\u0161\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163")
        buf.write("$\3\2\2\2\u0164\u0165\7n\2\2\u0165\u0166\7q\2\2\u0166")
        buf.write("\u0167\7p\2\2\u0167\u0168\7i\2\2\u0168&\3\2\2\2\u0169")
        buf.write("\u016a\7t\2\2\u016a\u016b\7g\2\2\u016b\u016c\7u\2\2\u016c")
        buf.write("\u016d\7v\2\2\u016d\u016e\7t\2\2\u016e\u016f\7k\2\2\u016f")
        buf.write("\u0170\7e\2\2\u0170\u0171\7v\2\2\u0171(\3\2\2\2\u0172")
        buf.write("\u0173\7t\2\2\u0173\u0174\7g\2\2\u0174\u0175\7v\2\2\u0175")
        buf.write("\u0176\7w\2\2\u0176\u0177\7t\2\2\u0177\u0178\7p\2\2\u0178")
        buf.write("*\3\2\2\2\u0179\u017a\7u\2\2\u017a\u017b\7j\2\2\u017b")
        buf.write("\u017c\7q\2\2\u017c\u017d\7t\2\2\u017d\u017e\7v\2\2\u017e")
        buf.write(",\3\2\2\2\u017f\u0180\7u\2\2\u0180\u0181\7k\2\2\u0181")
        buf.write("\u0182\7i\2\2\u0182\u0183\7p\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("\u0185\7f\2\2\u0185.\3\2\2\2\u0186\u0187\7u\2\2\u0187")
        buf.write("\u0188\7k\2\2\u0188\u0189\7|\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\u018b\7q\2\2\u018b\u018c\7h\2\2\u018c\60\3\2\2\2\u018d")
        buf.write("\u018e\7u\2\2\u018e\u018f\7v\2\2\u018f\u0190\7c\2\2\u0190")
        buf.write("\u0191\7v\2\2\u0191\u0192\7k\2\2\u0192\u0193\7e\2\2\u0193")
        buf.write("\62\3\2\2\2\u0194\u0195\7u\2\2\u0195\u0196\7v\2\2\u0196")
        buf.write("\u0197\7t\2\2\u0197\u0198\7w\2\2\u0198\u0199\7e\2\2\u0199")
        buf.write("\u019a\7v\2\2\u019a\64\3\2\2\2\u019b\u019c\7u\2\2\u019c")
        buf.write("\u019d\7y\2\2\u019d\u019e\7k\2\2\u019e\u019f\7v\2\2\u019f")
        buf.write("\u01a0\7e\2\2\u01a0\u01a1\7j\2\2\u01a1\66\3\2\2\2\u01a2")
        buf.write("\u01a3\7v\2\2\u01a3\u01a4\7{\2\2\u01a4\u01a5\7r\2\2\u01a5")
        buf.write("\u01a6\7g\2\2\u01a6\u01a7\7f\2\2\u01a7\u01a8\7g\2\2\u01a8")
        buf.write("\u01a9\7h\2\2\u01a98\3\2\2\2\u01aa\u01ab\7w\2\2\u01ab")
        buf.write("\u01ac\7p\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae\7q\2\2\u01ae")
        buf.write("\u01af\7p\2\2\u01af:\3\2\2\2\u01b0\u01b1\7w\2\2\u01b1")
        buf.write("\u01b2\7p\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b4\7k\2\2\u01b4")
        buf.write("\u01b5\7i\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7g\2\2\u01b7")
        buf.write("\u01b8\7f\2\2\u01b8<\3\2\2\2\u01b9\u01ba\7x\2\2\u01ba")
        buf.write("\u01bb\7q\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd\7f\2\2\u01bd")
        buf.write(">\3\2\2\2\u01be\u01bf\7x\2\2\u01bf\u01c0\7q\2\2\u01c0")
        buf.write("\u01c1\7n\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3\7v\2\2\u01c3")
        buf.write("\u01c4\7k\2\2\u01c4\u01c5\7n\2\2\u01c5\u01c6\7g\2\2\u01c6")
        buf.write("@\3\2\2\2\u01c7\u01c8\7y\2\2\u01c8\u01c9\7j\2\2\u01c9")
        buf.write("\u01ca\7k\2\2\u01ca\u01cb\7n\2\2\u01cb\u01cc\7g\2\2\u01cc")
        buf.write("B\3\2\2\2\u01cd\u01ce\7*\2\2\u01ceD\3\2\2\2\u01cf\u01d0")
        buf.write("\7+\2\2\u01d0F\3\2\2\2\u01d1\u01d2\7]\2\2\u01d2H\3\2\2")
        buf.write("\2\u01d3\u01d4\7_\2\2\u01d4J\3\2\2\2\u01d5\u01d6\7}\2")
        buf.write("\2\u01d6L\3\2\2\2\u01d7\u01d8\7\177\2\2\u01d8N\3\2\2\2")
        buf.write("\u01d9\u01da\7>\2\2\u01daP\3\2\2\2\u01db\u01dc\7>\2\2")
        buf.write("\u01dc\u01dd\7?\2\2\u01ddR\3\2\2\2\u01de\u01df\7@\2\2")
        buf.write("\u01dfT\3\2\2\2\u01e0\u01e1\7@\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2V\3\2\2\2\u01e3\u01e4\7>\2\2\u01e4\u01e5\7>\2\2")
        buf.write("\u01e5X\3\2\2\2\u01e6\u01e7\7@\2\2\u01e7\u01e8\7@\2\2")
        buf.write("\u01e8Z\3\2\2\2\u01e9\u01ea\7-\2\2\u01ea\\\3\2\2\2\u01eb")
        buf.write("\u01ec\7-\2\2\u01ec\u01ed\7-\2\2\u01ed^\3\2\2\2\u01ee")
        buf.write("\u01ef\7/\2\2\u01ef`\3\2\2\2\u01f0\u01f1\7/\2\2\u01f1")
        buf.write("\u01f2\7/\2\2\u01f2b\3\2\2\2\u01f3\u01f4\7,\2\2\u01f4")
        buf.write("d\3\2\2\2\u01f5\u01f6\7\61\2\2\u01f6f\3\2\2\2\u01f7\u01f8")
        buf.write("\7\'\2\2\u01f8h\3\2\2\2\u01f9\u01fa\7(\2\2\u01faj\3\2")
        buf.write("\2\2\u01fb\u01fc\7~\2\2\u01fcl\3\2\2\2\u01fd\u01fe\7(")
        buf.write("\2\2\u01fe\u01ff\7(\2\2\u01ffn\3\2\2\2\u0200\u0201\7~")
        buf.write("\2\2\u0201\u0202\7~\2\2\u0202p\3\2\2\2\u0203\u0204\7`")
        buf.write("\2\2\u0204r\3\2\2\2\u0205\u0206\7#\2\2\u0206t\3\2\2\2")
        buf.write("\u0207\u0208\7\u0080\2\2\u0208v\3\2\2\2\u0209\u020a\7")
        buf.write("A\2\2\u020ax\3\2\2\2\u020b\u020c\7<\2\2\u020cz\3\2\2\2")
        buf.write("\u020d\u020e\7=\2\2\u020e|\3\2\2\2\u020f\u0210\7.\2\2")
        buf.write("\u0210~\3\2\2\2\u0211\u0212\7?\2\2\u0212\u0080\3\2\2\2")
        buf.write("\u0213\u0214\7,\2\2\u0214\u0215\7?\2\2\u0215\u0082\3\2")
        buf.write("\2\2\u0216\u0217\7\61\2\2\u0217\u0218\7?\2\2\u0218\u0084")
        buf.write("\3\2\2\2\u0219\u021a\7\'\2\2\u021a\u021b\7?\2\2\u021b")
        buf.write("\u0086\3\2\2\2\u021c\u021d\7-\2\2\u021d\u021e\7?\2\2\u021e")
        buf.write("\u0088\3\2\2\2\u021f\u0220\7/\2\2\u0220\u0221\7?\2\2\u0221")
        buf.write("\u008a\3\2\2\2\u0222\u0223\7>\2\2\u0223\u0224\7>\2\2\u0224")
        buf.write("\u0225\7?\2\2\u0225\u008c\3\2\2\2\u0226\u0227\7@\2\2\u0227")
        buf.write("\u0228\7@\2\2\u0228\u0229\7?\2\2\u0229\u008e\3\2\2\2\u022a")
        buf.write("\u022b\7(\2\2\u022b\u022c\7?\2\2\u022c\u0090\3\2\2\2\u022d")
        buf.write("\u022e\7`\2\2\u022e\u022f\7?\2\2\u022f\u0092\3\2\2\2\u0230")
        buf.write("\u0231\7~\2\2\u0231\u0232\7?\2\2\u0232\u0094\3\2\2\2\u0233")
        buf.write("\u0234\7?\2\2\u0234\u0235\7?\2\2\u0235\u0096\3\2\2\2\u0236")
        buf.write("\u0237\7#\2\2\u0237\u0238\7?\2\2\u0238\u0098\3\2\2\2\u0239")
        buf.write("\u023a\7/\2\2\u023a\u023b\7@\2\2\u023b\u009a\3\2\2\2\u023c")
        buf.write("\u023d\7\60\2\2\u023d\u009c\3\2\2\2\u023e\u023f\7\60\2")
        buf.write("\2\u023f\u0240\7\60\2\2\u0240\u0241\7\60\2\2\u0241\u009e")
        buf.write("\3\2\2\2\u0242\u0247\5\u00a1Q\2\u0243\u0246\5\u00a1Q\2")
        buf.write("\u0244\u0246\5\u00a5S\2\u0245\u0243\3\2\2\2\u0245\u0244")
        buf.write("\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u00a0\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u024a\u024d\5\u00a3R\2\u024b\u024d\5\u00a7T\2\u024c\u024a")
        buf.write("\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u00a2\3\2\2\2\u024e")
        buf.write("\u024f\t\2\2\2\u024f\u00a4\3\2\2\2\u0250\u0251\t\3\2\2")
        buf.write("\u0251\u00a6\3\2\2\2\u0252\u0253\7^\2\2\u0253\u0254\7")
        buf.write("w\2\2\u0254\u0255\3\2\2\2\u0255\u025d\5\u00a9U\2\u0256")
        buf.write("\u0257\7^\2\2\u0257\u0258\7W\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("\u025a\5\u00a9U\2\u025a\u025b\5\u00a9U\2\u025b\u025d\3")
        buf.write("\2\2\2\u025c\u0252\3\2\2\2\u025c\u0256\3\2\2\2\u025d\u00a8")
        buf.write("\3\2\2\2\u025e\u025f\5\u00bd_\2\u025f\u0260\5\u00bd_\2")
        buf.write("\u0260\u0261\5\u00bd_\2\u0261\u0262\5\u00bd_\2\u0262\u00aa")
        buf.write("\3\2\2\2\u0263\u0267\5\u00adW\2\u0264\u0267\5\u00c7d\2")
        buf.write("\u0265\u0267\5\u00ddo\2\u0266\u0263\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0265\3\2\2\2\u0267\u00ac\3\2\2\2\u0268")
        buf.write("\u026a\5\u00b1Y\2\u0269\u026b\5\u00bf`\2\u026a\u0269\3")
        buf.write("\2\2\2\u026a\u026b\3\2\2\2\u026b\u0276\3\2\2\2\u026c\u026e")
        buf.write("\5\u00b3Z\2\u026d\u026f\5\u00bf`\2\u026e\u026d\3\2\2\2")
        buf.write("\u026e\u026f\3\2\2\2\u026f\u0276\3\2\2\2\u0270\u0272\5")
        buf.write("\u00b5[\2\u0271\u0273\5\u00bf`\2\u0272\u0271\3\2\2\2\u0272")
        buf.write("\u0273\3\2\2\2\u0273\u0276\3\2\2\2\u0274\u0276\5\u00af")
        buf.write("X\2\u0275\u0268\3\2\2\2\u0275\u026c\3\2\2\2\u0275\u0270")
        buf.write("\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u00ae\3\2\2\2\u0277")
        buf.write("\u0278\7\62\2\2\u0278\u027a\t\4\2\2\u0279\u027b\t\5\2")
        buf.write("\2\u027a\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027a")
        buf.write("\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u00b0\3\2\2\2\u027e")
        buf.write("\u0282\5\u00b9]\2\u027f\u0281\5\u00a5S\2\u0280\u027f\3")
        buf.write("\2\2\2\u0281\u0284\3\2\2\2\u0282\u0280\3\2\2\2\u0282\u0283")
        buf.write("\3\2\2\2\u0283\u00b2\3\2\2\2\u0284\u0282\3\2\2\2\u0285")
        buf.write("\u0289\7\62\2\2\u0286\u0288\5\u00bb^\2\u0287\u0286\3\2")
        buf.write("\2\2\u0288\u028b\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u028a")
        buf.write("\3\2\2\2\u028a\u00b4\3\2\2\2\u028b\u0289\3\2\2\2\u028c")
        buf.write("\u028e\5\u00b7\\\2\u028d\u028f\5\u00bd_\2\u028e\u028d")
        buf.write("\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u028e\3\2\2\2\u0290")
        buf.write("\u0291\3\2\2\2\u0291\u00b6\3\2\2\2\u0292\u0293\7\62\2")
        buf.write("\2\u0293\u0294\t\6\2\2\u0294\u00b8\3\2\2\2\u0295\u0296")
        buf.write("\t\7\2\2\u0296\u00ba\3\2\2\2\u0297\u0298\t\b\2\2\u0298")
        buf.write("\u00bc\3\2\2\2\u0299\u029a\t\t\2\2\u029a\u00be\3\2\2\2")
        buf.write("\u029b\u029d\5\u00c1a\2\u029c\u029e\5\u00c3b\2\u029d\u029c")
        buf.write("\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u02ab\3\2\2\2\u029f")
        buf.write("\u02a0\5\u00c1a\2\u02a0\u02a1\5\u00c5c\2\u02a1\u02ab\3")
        buf.write("\2\2\2\u02a2\u02a4\5\u00c3b\2\u02a3\u02a5\5\u00c1a\2\u02a4")
        buf.write("\u02a3\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02ab\3\2\2\2")
        buf.write("\u02a6\u02a8\5\u00c5c\2\u02a7\u02a9\5\u00c1a\2\u02a8\u02a7")
        buf.write("\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ab\3\2\2\2\u02aa")
        buf.write("\u029b\3\2\2\2\u02aa\u029f\3\2\2\2\u02aa\u02a2\3\2\2\2")
        buf.write("\u02aa\u02a6\3\2\2\2\u02ab\u00c0\3\2\2\2\u02ac\u02ad\t")
        buf.write("\n\2\2\u02ad\u00c2\3\2\2\2\u02ae\u02af\t\13\2\2\u02af")
        buf.write("\u00c4\3\2\2\2\u02b0\u02b1\7n\2\2\u02b1\u02b5\7n\2\2\u02b2")
        buf.write("\u02b3\7N\2\2\u02b3\u02b5\7N\2\2\u02b4\u02b0\3\2\2\2\u02b4")
        buf.write("\u02b2\3\2\2\2\u02b5\u00c6\3\2\2\2\u02b6\u02b9\5\u00c9")
        buf.write("e\2\u02b7\u02b9\5\u00cbf\2\u02b8\u02b6\3\2\2\2\u02b8\u02b7")
        buf.write("\3\2\2\2\u02b9\u00c8\3\2\2\2\u02ba\u02bc\5\u00cdg\2\u02bb")
        buf.write("\u02bd\5\u00cfh\2\u02bc\u02bb\3\2\2\2\u02bc\u02bd\3\2")
        buf.write("\2\2\u02bd\u02bf\3\2\2\2\u02be\u02c0\5\u00dbn\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c7\3\2\2\2")
        buf.write("\u02c1\u02c2\5\u00d3j\2\u02c2\u02c4\5\u00cfh\2\u02c3\u02c5")
        buf.write("\5\u00dbn\2\u02c4\u02c3\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5")
        buf.write("\u02c7\3\2\2\2\u02c6\u02ba\3\2\2\2\u02c6\u02c1\3\2\2\2")
        buf.write("\u02c7\u00ca\3\2\2\2\u02c8\u02c9\5\u00b7\\\2\u02c9\u02ca")
        buf.write("\5\u00d5k\2\u02ca\u02cc\5\u00d7l\2\u02cb\u02cd\5\u00db")
        buf.write("n\2\u02cc\u02cb\3\2\2\2\u02cc\u02cd\3\2\2\2\u02cd\u02d5")
        buf.write("\3\2\2\2\u02ce\u02cf\5\u00b7\\\2\u02cf\u02d0\5\u00d9m")
        buf.write("\2\u02d0\u02d2\5\u00d7l\2\u02d1\u02d3\5\u00dbn\2\u02d2")
        buf.write("\u02d1\3\2\2\2\u02d2\u02d3\3\2\2\2\u02d3\u02d5\3\2\2\2")
        buf.write("\u02d4\u02c8\3\2\2\2\u02d4\u02ce\3\2\2\2\u02d5\u00cc\3")
        buf.write("\2\2\2\u02d6\u02d8\5\u00d3j\2\u02d7\u02d6\3\2\2\2\u02d7")
        buf.write("\u02d8\3\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02da\5\u009b")
        buf.write("N\2\u02da\u02db\5\u00d3j\2\u02db\u02e0\3\2\2\2\u02dc\u02dd")
        buf.write("\5\u00d3j\2\u02dd\u02de\5\u009bN\2\u02de\u02e0\3\2\2\2")
        buf.write("\u02df\u02d7\3\2\2\2\u02df\u02dc\3\2\2\2\u02e0\u00ce\3")
        buf.write("\2\2\2\u02e1\u02e3\7g\2\2\u02e2\u02e4\5\u00d1i\2\u02e3")
        buf.write("\u02e2\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u02e5\3\2\2\2")
        buf.write("\u02e5\u02ec\5\u00d3j\2\u02e6\u02e8\7G\2\2\u02e7\u02e9")
        buf.write("\5\u00d1i\2\u02e8\u02e7\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9")
        buf.write("\u02ea\3\2\2\2\u02ea\u02ec\5\u00d3j\2\u02eb\u02e1\3\2")
        buf.write("\2\2\u02eb\u02e6\3\2\2\2\u02ec\u00d0\3\2\2\2\u02ed\u02ee")
        buf.write("\t\f\2\2\u02ee\u00d2\3\2\2\2\u02ef\u02f1\5\u00a5S\2\u02f0")
        buf.write("\u02ef\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\u02f0\3\2\2\2")
        buf.write("\u02f2\u02f3\3\2\2\2\u02f3\u00d4\3\2\2\2\u02f4\u02f6\5")
        buf.write("\u00d9m\2\u02f5\u02f4\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6")
        buf.write("\u02f7\3\2\2\2\u02f7\u02f8\5\u009bN\2\u02f8\u02f9\5\u00d9")
        buf.write("m\2\u02f9\u02fe\3\2\2\2\u02fa\u02fb\5\u00d9m\2\u02fb\u02fc")
        buf.write("\5\u009bN\2\u02fc\u02fe\3\2\2\2\u02fd\u02f5\3\2\2\2\u02fd")
        buf.write("\u02fa\3\2\2\2\u02fe\u00d6\3\2\2\2\u02ff\u0301\7r\2\2")
        buf.write("\u0300\u0302\5\u00d1i\2\u0301\u0300\3\2\2\2\u0301\u0302")
        buf.write("\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u030a\5\u00d3j\2\u0304")
        buf.write("\u0306\7R\2\2\u0305\u0307\5\u00d1i\2\u0306\u0305\3\2\2")
        buf.write("\2\u0306\u0307\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u030a")
        buf.write("\5\u00d3j\2\u0309\u02ff\3\2\2\2\u0309\u0304\3\2\2\2\u030a")
        buf.write("\u00d8\3\2\2\2\u030b\u030d\5\u00bd_\2\u030c\u030b\3\2")
        buf.write("\2\2\u030d\u030e\3\2\2\2\u030e\u030c\3\2\2\2\u030e\u030f")
        buf.write("\3\2\2\2\u030f\u00da\3\2\2\2\u0310\u0311\t\r\2\2\u0311")
        buf.write("\u00dc\3\2\2\2\u0312\u0313\7)\2\2\u0313\u0314\5\u00df")
        buf.write("p\2\u0314\u0315\7)\2\2\u0315\u0329\3\2\2\2\u0316\u0317")
        buf.write("\7N\2\2\u0317\u0318\7)\2\2\u0318\u0319\3\2\2\2\u0319\u031a")
        buf.write("\5\u00dfp\2\u031a\u031b\7)\2\2\u031b\u0329\3\2\2\2\u031c")
        buf.write("\u031d\7w\2\2\u031d\u031e\7)\2\2\u031e\u031f\3\2\2\2\u031f")
        buf.write("\u0320\5\u00dfp\2\u0320\u0321\7)\2\2\u0321\u0329\3\2\2")
        buf.write("\2\u0322\u0323\7W\2\2\u0323\u0324\7)\2\2\u0324\u0325\3")
        buf.write("\2\2\2\u0325\u0326\5\u00dfp\2\u0326\u0327\7)\2\2\u0327")
        buf.write("\u0329\3\2\2\2\u0328\u0312\3\2\2\2\u0328\u0316\3\2\2\2")
        buf.write("\u0328\u031c\3\2\2\2\u0328\u0322\3\2\2\2\u0329\u00de\3")
        buf.write("\2\2\2\u032a\u032c\5\u00e1q\2\u032b\u032a\3\2\2\2\u032c")
        buf.write("\u032d\3\2\2\2\u032d\u032b\3\2\2\2\u032d\u032e\3\2\2\2")
        buf.write("\u032e\u00e0\3\2\2\2\u032f\u0332\n\16\2\2\u0330\u0332")
        buf.write("\5\u00e3r\2\u0331\u032f\3\2\2\2\u0331\u0330\3\2\2\2\u0332")
        buf.write("\u00e2\3\2\2\2\u0333\u0338\5\u00e5s\2\u0334\u0338\5\u00e7")
        buf.write("t\2\u0335\u0338\5\u00e9u\2\u0336\u0338\5\u00a7T\2\u0337")
        buf.write("\u0333\3\2\2\2\u0337\u0334\3\2\2\2\u0337\u0335\3\2\2\2")
        buf.write("\u0337\u0336\3\2\2\2\u0338\u00e4\3\2\2\2\u0339\u033a\7")
        buf.write("^\2\2\u033a\u033b\t\17\2\2\u033b\u00e6\3\2\2\2\u033c\u033d")
        buf.write("\7^\2\2\u033d\u0348\5\u00bb^\2\u033e\u033f\7^\2\2\u033f")
        buf.write("\u0340\5\u00bb^\2\u0340\u0341\5\u00bb^\2\u0341\u0348\3")
        buf.write("\2\2\2\u0342\u0343\7^\2\2\u0343\u0344\5\u00bb^\2\u0344")
        buf.write("\u0345\5\u00bb^\2\u0345\u0346\5\u00bb^\2\u0346\u0348\3")
        buf.write("\2\2\2\u0347\u033c\3\2\2\2\u0347\u033e\3\2\2\2\u0347\u0342")
        buf.write("\3\2\2\2\u0348\u00e8\3\2\2\2\u0349\u034a\7^\2\2\u034a")
        buf.write("\u034b\7z\2\2\u034b\u034d\3\2\2\2\u034c\u034e\5\u00bd")
        buf.write("_\2\u034d\u034c\3\2\2\2\u034e\u034f\3\2\2\2\u034f\u034d")
        buf.write("\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u00ea\3\2\2\2\u0351")
        buf.write("\u0353\5\u00edw\2\u0352\u0351\3\2\2\2\u0352\u0353\3\2")
        buf.write("\2\2\u0353\u0354\3\2\2\2\u0354\u0356\7$\2\2\u0355\u0357")
        buf.write("\5\u00efx\2\u0356\u0355\3\2\2\2\u0356\u0357\3\2\2\2\u0357")
        buf.write("\u0358\3\2\2\2\u0358\u0359\7$\2\2\u0359\u00ec\3\2\2\2")
        buf.write("\u035a\u035b\7w\2\2\u035b\u035e\7:\2\2\u035c\u035e\t\20")
        buf.write("\2\2\u035d\u035a\3\2\2\2\u035d\u035c\3\2\2\2\u035e\u00ee")
        buf.write("\3\2\2\2\u035f\u0361\5\u00f1y\2\u0360\u035f\3\2\2\2\u0361")
        buf.write("\u0362\3\2\2\2\u0362\u0360\3\2\2\2\u0362\u0363\3\2\2\2")
        buf.write("\u0363\u00f0\3\2\2\2\u0364\u036c\n\21\2\2\u0365\u036c")
        buf.write("\5\u00e3r\2\u0366\u0367\7^\2\2\u0367\u036c\7\f\2\2\u0368")
        buf.write("\u0369\7^\2\2\u0369\u036a\7\17\2\2\u036a\u036c\7\f\2\2")
        buf.write("\u036b\u0364\3\2\2\2\u036b\u0365\3\2\2\2\u036b\u0366\3")
        buf.write("\2\2\2\u036b\u0368\3\2\2\2\u036c\u00f2\3\2\2\2\u036d\u036f")
        buf.write("\7%\2\2\u036e\u0370\5\u00ff\u0080\2\u036f\u036e\3\2\2")
        buf.write("\2\u036f\u0370\3\2\2\2\u0370\u0371\3\2\2\2\u0371\u0372")
        buf.write("\7f\2\2\u0372\u0373\7g\2\2\u0373\u0374\7h\2\2\u0374\u0375")
        buf.write("\7k\2\2\u0375\u0376\7p\2\2\u0376\u0377\7g\2\2\u0377\u037b")
        buf.write("\3\2\2\2\u0378\u037a\n\22\2\2\u0379\u0378\3\2\2\2\u037a")
        buf.write("\u037d\3\2\2\2\u037b\u0379\3\2\2\2\u037b\u037c\3\2\2\2")
        buf.write("\u037c\u037e\3\2\2\2\u037d\u037b\3\2\2\2\u037e\u037f\b")
        buf.write("z\2\2\u037f\u00f4\3\2\2\2\u0380\u0381\7c\2\2\u0381\u0382")
        buf.write("\7u\2\2\u0382\u0383\7o\2\2\u0383\u0387\3\2\2\2\u0384\u0386")
        buf.write("\n\23\2\2\u0385\u0384\3\2\2\2\u0386\u0389\3\2\2\2\u0387")
        buf.write("\u0385\3\2\2\2\u0387\u0388\3\2\2\2\u0388\u038a\3\2\2\2")
        buf.write("\u0389\u0387\3\2\2\2\u038a\u038e\5K&\2\u038b\u038d\n\24")
        buf.write("\2\2\u038c\u038b\3\2\2\2\u038d\u0390\3\2\2\2\u038e\u038c")
        buf.write("\3\2\2\2\u038e\u038f\3\2\2\2\u038f\u0391\3\2\2\2\u0390")
        buf.write("\u038e\3\2\2\2\u0391\u0392\5M\'\2\u0392\u0393\3\2\2\2")
        buf.write("\u0393\u0394\b{\2\2\u0394\u00f6\3\2\2\2\u0395\u0396\7")
        buf.write("%\2\2\u0396\u0397\7n\2\2\u0397\u0398\7k\2\2\u0398\u0399")
        buf.write("\7p\2\2\u0399\u039a\7g\2\2\u039a\u039e\3\2\2\2\u039b\u039d")
        buf.write("\5\u00ff\u0080\2\u039c\u039b\3\2\2\2\u039d\u03a0\3\2\2")
        buf.write("\2\u039e\u039c\3\2\2\2\u039e\u039f\3\2\2\2\u039f\u03a4")
        buf.write("\3\2\2\2\u03a0\u039e\3\2\2\2\u03a1\u03a3\n\25\2\2\u03a2")
        buf.write("\u03a1\3\2\2\2\u03a3\u03a6\3\2\2\2\u03a4\u03a2\3\2\2\2")
        buf.write("\u03a4\u03a5\3\2\2\2\u03a5\u03a7\3\2\2\2\u03a6\u03a4\3")
        buf.write("\2\2\2\u03a7\u03a8\b|\2\2\u03a8\u00f8\3\2\2\2\u03a9\u03ab")
        buf.write("\7%\2\2\u03aa\u03ac\5\u00ff\u0080\2\u03ab\u03aa\3\2\2")
        buf.write("\2\u03ab\u03ac\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03af")
        buf.write("\5\u00b1Y\2\u03ae\u03b0\5\u00ff\u0080\2\u03af\u03ae\3")
        buf.write("\2\2\2\u03af\u03b0\3\2\2\2\u03b0\u03b1\3\2\2\2\u03b1\u03b5")
        buf.write("\5\u00ebv\2\u03b2\u03b4\n\25\2\2\u03b3\u03b2\3\2\2\2\u03b4")
        buf.write("\u03b7\3\2\2\2\u03b5\u03b3\3\2\2\2\u03b5\u03b6\3\2\2\2")
        buf.write("\u03b6\u03b8\3\2\2\2\u03b7\u03b5\3\2\2\2\u03b8\u03b9\b")
        buf.write("}\2\2\u03b9\u00fa\3\2\2\2\u03ba\u03cd\7%\2\2\u03bb\u03bc")
        buf.write("\7k\2\2\u03bc\u03bd\7p\2\2\u03bd\u03be\7e\2\2\u03be\u03bf")
        buf.write("\7n\2\2\u03bf\u03c0\7w\2\2\u03c0\u03c1\7f\2\2\u03c1\u03ce")
        buf.write("\7g\2\2\u03c2\u03c3\7f\2\2\u03c3\u03c4\7g\2\2\u03c4\u03c5")
        buf.write("\7h\2\2\u03c5\u03c6\7k\2\2\u03c6\u03c7\7p\2\2\u03c7\u03ce")
        buf.write("\7g\2\2\u03c8\u03ce\5\37\20\2\u03c9\u03ca\7g\2\2\u03ca")
        buf.write("\u03cb\7n\2\2\u03cb\u03cc\7k\2\2\u03cc\u03ce\7h\2\2\u03cd")
        buf.write("\u03bb\3\2\2\2\u03cd\u03c2\3\2\2\2\u03cd\u03c8\3\2\2\2")
        buf.write("\u03cd\u03c9\3\2\2\2\u03ce\u03d2\3\2\2\2\u03cf\u03d1\n")
        buf.write("\25\2\2\u03d0\u03cf\3\2\2\2\u03d1\u03d4\3\2\2\2\u03d2")
        buf.write("\u03d0\3\2\2\2\u03d2\u03d3\3\2\2\2\u03d3\u03d5\3\2\2\2")
        buf.write("\u03d4\u03d2\3\2\2\2\u03d5\u03d6\b~\2\2\u03d6\u00fc\3")
        buf.write("\2\2\2\u03d7\u03d9\7%\2\2\u03d8\u03da\5\u00ff\u0080\2")
        buf.write("\u03d9\u03d8\3\2\2\2\u03d9\u03da\3\2\2\2\u03da\u03db\3")
        buf.write("\2\2\2\u03db\u03dc\7r\2\2\u03dc\u03dd\7t\2\2\u03dd\u03de")
        buf.write("\7c\2\2\u03de\u03df\7i\2\2\u03df\u03e0\7o\2\2\u03e0\u03e1")
        buf.write("\7c\2\2\u03e1\u03e2\3\2\2\2\u03e2\u03e6\5\u00ff\u0080")
        buf.write("\2\u03e3\u03e5\n\25\2\2\u03e4\u03e3\3\2\2\2\u03e5\u03e8")
        buf.write("\3\2\2\2\u03e6\u03e4\3\2\2\2\u03e6\u03e7\3\2\2\2\u03e7")
        buf.write("\u03e9\3\2\2\2\u03e8\u03e6\3\2\2\2\u03e9\u03ea\b\177\2")
        buf.write("\2\u03ea\u00fe\3\2\2\2\u03eb\u03ed\t\26\2\2\u03ec\u03eb")
        buf.write("\3\2\2\2\u03ed\u03ee\3\2\2\2\u03ee\u03ec\3\2\2\2\u03ee")
        buf.write("\u03ef\3\2\2\2\u03ef\u03f0\3\2\2\2\u03f0\u03f1\b\u0080")
        buf.write("\2\2\u03f1\u0100\3\2\2\2\u03f2\u03f4\7\17\2\2\u03f3\u03f5")
        buf.write("\7\f\2\2\u03f4\u03f3\3\2\2\2\u03f4\u03f5\3\2\2\2\u03f5")
        buf.write("\u03f8\3\2\2\2\u03f6\u03f8\7\f\2\2\u03f7\u03f2\3\2\2\2")
        buf.write("\u03f7\u03f6\3\2\2\2\u03f8\u03f9\3\2\2\2\u03f9\u03fa\b")
        buf.write("\u0081\2\2\u03fa\u0102\3\2\2\2\u03fb\u03fc\7\61\2\2\u03fc")
        buf.write("\u03fd\7,\2\2\u03fd\u0401\3\2\2\2\u03fe\u0400\13\2\2\2")
        buf.write("\u03ff\u03fe\3\2\2\2\u0400\u0403\3\2\2\2\u0401\u0402\3")
        buf.write("\2\2\2\u0401\u03ff\3\2\2\2\u0402\u0404\3\2\2\2\u0403\u0401")
        buf.write("\3\2\2\2\u0404\u0405\7,\2\2\u0405\u0406\7\61\2\2\u0406")
        buf.write("\u0407\3\2\2\2\u0407\u0408\b\u0082\2\2\u0408\u0104\3\2")
        buf.write("\2\2\u0409\u040a\7\61\2\2\u040a\u040b\7\61\2\2\u040b\u040f")
        buf.write("\3\2\2\2\u040c\u040e\n\25\2\2\u040d\u040c\3\2\2\2\u040e")
        buf.write("\u0411\3\2\2\2\u040f\u040d\3\2\2\2\u040f\u0410\3\2\2\2")
        buf.write("\u0410\u0412\3\2\2\2\u0411\u040f\3\2\2\2\u0412\u0413\b")
        buf.write("\u0083\2\2\u0413\u0106\3\2\2\2F\2\u0245\u0247\u024c\u025c")
        buf.write("\u0266\u026a\u026e\u0272\u0275\u027c\u0282\u0289\u0290")
        buf.write("\u029d\u02a4\u02a8\u02aa\u02b4\u02b8\u02bc\u02bf\u02c4")
        buf.write("\u02c6\u02cc\u02d2\u02d4\u02d7\u02df\u02e3\u02e8\u02eb")
        buf.write("\u02f2\u02f5\u02fd\u0301\u0306\u0309\u030e\u0328\u032d")
        buf.write("\u0331\u0337\u0347\u034f\u0352\u0356\u035d\u0362\u036b")
        buf.write("\u036f\u037b\u0387\u038e\u039e\u03a4\u03ab\u03af\u03b5")
        buf.write("\u03cd\u03d2\u03d9\u03e6\u03ee\u03f4\u03f7\u0401\u040f")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class ClangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Auto = 1
    Break = 2
    Case = 3
    Char = 4
    Const = 5
    Continue = 6
    Default = 7
    Do = 8
    Double = 9
    Else = 10
    Enum = 11
    Float = 12
    For = 13
    Goto = 14
    If = 15
    Inline = 16
    Int = 17
    Long = 18
    Restrict = 19
    Return = 20
    Short = 21
    Signed = 22
    Sizeof = 23
    Static = 24
    Struct = 25
    Switch = 26
    Typedef = 27
    Union = 28
    Unsigned = 29
    Void = 30
    Volatile = 31
    While = 32
    LeftParen = 33
    RightParen = 34
    LeftBracket = 35
    RightBracket = 36
    LeftBrace = 37
    RightBrace = 38
    Less = 39
    LessEqual = 40
    Greater = 41
    GreaterEqual = 42
    LeftShift = 43
    RightShift = 44
    Plus = 45
    Increment = 46
    Minus = 47
    Descrement = 48
    Star = 49
    Div = 50
    Mod = 51
    And = 52
    Or = 53
    LogicalAnd = 54
    LogicalOr = 55
    Caret = 56
    Not = 57
    Tilde = 58
    Question = 59
    Colon = 60
    Semi = 61
    Comma = 62
    Assign = 63
    StarAssign = 64
    DivAssign = 65
    ModAssign = 66
    PlusAssign = 67
    MinusAssign = 68
    LeftShiftAssign = 69
    RightShiftAssign = 70
    AndAssign = 71
    XorAssign = 72
    OrAssign = 73
    Equal = 74
    NotEqual = 75
    Arrow = 76
    Dot = 77
    Ellipsis = 78
    Identifier = 79
    Constant = 80
    DigitSequence = 81
    StringLiteral = 82
    ComplexDefine = 83
    AsmBlock = 84
    LineAfterPreprocessing = 85
    LineDirective = 86
    PreprocessiorBlock = 87
    PragmaDirective = 88
    Whitespace = 89
    Newline = 90
    BlockComment = 91
    LineComment = 92

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'case'", "'char'", "'const'", "'continue'", 
            "'default'", "'do'", "'double'", "'else'", "'enum'", "'float'", 
            "'for'", "'goto'", "'if'", "'inline'", "'int'", "'long'", "'restrict'", 
            "'return'", "'short'", "'signed'", "'sizeof'", "'static'", "'struct'", 
            "'switch'", "'typedef'", "'union'", "'unsigned'", "'void'", 
            "'volatile'", "'while'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'<'", "'<='", "'>'", "'>='", "'<<'", "'>>'", "'+'", 
            "'++'", "'-'", "'--'", "'*'", "'/'", "'%'", "'&'", "'|'", "'&&'", 
            "'||'", "'^'", "'!'", "'~'", "'?'", "':'", "';'", "','", "'='", 
            "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'&='", 
            "'^='", "'|='", "'=='", "'!='", "'->'", "'.'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "Auto", "Break", "Case", "Char", "Const", "Continue", "Default", 
            "Do", "Double", "Else", "Enum", "Float", "For", "Goto", "If", 
            "Inline", "Int", "Long", "Restrict", "Return", "Short", "Signed", 
            "Sizeof", "Static", "Struct", "Switch", "Typedef", "Union", 
            "Unsigned", "Void", "Volatile", "While", "LeftParen", "RightParen", 
            "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", "Less", 
            "LessEqual", "Greater", "GreaterEqual", "LeftShift", "RightShift", 
            "Plus", "Increment", "Minus", "Descrement", "Star", "Div", "Mod", 
            "And", "Or", "LogicalAnd", "LogicalOr", "Caret", "Not", "Tilde", 
            "Question", "Colon", "Semi", "Comma", "Assign", "StarAssign", 
            "DivAssign", "ModAssign", "PlusAssign", "MinusAssign", "LeftShiftAssign", 
            "RightShiftAssign", "AndAssign", "XorAssign", "OrAssign", "Equal", 
            "NotEqual", "Arrow", "Dot", "Ellipsis", "Identifier", "Constant", 
            "DigitSequence", "StringLiteral", "ComplexDefine", "AsmBlock", 
            "LineAfterPreprocessing", "LineDirective", "PreprocessiorBlock", 
            "PragmaDirective", "Whitespace", "Newline", "BlockComment", 
            "LineComment" ]

    ruleNames = [ "Auto", "Break", "Case", "Char", "Const", "Continue", 
                  "Default", "Do", "Double", "Else", "Enum", "Float", "For", 
                  "Goto", "If", "Inline", "Int", "Long", "Restrict", "Return", 
                  "Short", "Signed", "Sizeof", "Static", "Struct", "Switch", 
                  "Typedef", "Union", "Unsigned", "Void", "Volatile", "While", 
                  "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
                  "LeftBrace", "RightBrace", "Less", "LessEqual", "Greater", 
                  "GreaterEqual", "LeftShift", "RightShift", "Plus", "Increment", 
                  "Minus", "Descrement", "Star", "Div", "Mod", "And", "Or", 
                  "LogicalAnd", "LogicalOr", "Caret", "Not", "Tilde", "Question", 
                  "Colon", "Semi", "Comma", "Assign", "StarAssign", "DivAssign", 
                  "ModAssign", "PlusAssign", "MinusAssign", "LeftShiftAssign", 
                  "RightShiftAssign", "AndAssign", "XorAssign", "OrAssign", 
                  "Equal", "NotEqual", "Arrow", "Dot", "Ellipsis", "Identifier", 
                  "IdentifierNondigit", "Nondigit", "Digit", "UniversalCharacterName", 
                  "HexQuad", "Constant", "IntegerConstant", "BinaryConstant", 
                  "DecimalConstant", "OctalConstant", "HexadecimalConstant", 
                  "HexadecimalPrefix", "NonzeroDigit", "OctalDigit", "HexadecimalDigit", 
                  "IntegerSuffix", "UnsignedSuffix", "LongSuffix", "LongLongSuffix", 
                  "FloatingConstant", "DecimalFloatingConstant", "HexadecimalFloatingConstant", 
                  "FractionalConstant", "ExponentPart", "Sign", "DigitSequence", 
                  "HexadecimalFractionalConstant", "BinaryExponentPart", 
                  "HexadecimalDigitSequence", "FloatingSuffix", "CharacterConstant", 
                  "CCharSequence", "CChar", "EscapeSequence", "SimpleEscapeSequence", 
                  "OctalEscapeSequence", "HexadecimalEscapeSequence", "StringLiteral", 
                  "EncodingPrefix", "SCharSequence", "SChar", "ComplexDefine", 
                  "AsmBlock", "LineAfterPreprocessing", "LineDirective", 
                  "PreprocessiorBlock", "PragmaDirective", "Whitespace", 
                  "Newline", "BlockComment", "LineComment" ]

    grammarFileName = "Clang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


