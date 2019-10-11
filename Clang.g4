grammar Clang;

// RULES

primaryExpression
    :   Identifier
    |   Constant
    |   StringLiteral+
    |   LeftParen expression RightParen
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression LeftBracket expression RightBracket
    |   postfixExpression LeftParen argumentExpressionList? RightParen
    |   postfixExpression ( Dot | Arrow ) Identifier
    |   postfixExpression ( Increment | Descrement )
    |   LeftParen typeName RightParen LeftBrace initializerList RightBrace
    |   LeftParen typeName RightParen LeftBrace initializerList Comma RightBrace
    ;

argumentExpressionList
    :   assignmentExpression
    |   argumentExpressionList Comma assignmentExpression
    ;

unaryExpression
    :   postfixExpression
    |   ( Increment | Descrement ) unaryExpression
    |   unaryOperator castExpression
    |   Sizeof unaryExpression
    |   Sizeof LeftParen typeName RightParen
    ;

unaryOperator
    :   And | Star | Plus | Minus | Tilde | Not
    ;

castExpression
    :   LeftParen typeName RightParen castExpression
    |   unaryExpression
    |   DigitSequence
    ;

multiplicativeExpression
    :   castExpression
    |   multiplicativeExpression ( Star | Div | Mod ) castExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression ( Plus | Minus ) multiplicativeExpression
    ;

shiftExpression
    :   additiveExpression
    |   shiftExpression ( LeftShift | RightShift ) additiveExpression
    ;

relationalExpression
    :   shiftExpression
    |   relationalExpression ( Less | LessEqual | Greater | GreaterEqual ) shiftExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression ( Equal | NotEqual ) relationalExpression
    ;

andExpression
    :   equalityExpression
    |   andExpression And equalityExpression
    ;

exclusiveOrExpression
    :   andExpression
    |   exclusiveOrExpression Caret andExpression
    ;

inclusiveOrExpression
    :   exclusiveOrExpression
    |   inclusiveOrExpression Or exclusiveOrExpression
    ;

logicalAndExpression
    :   inclusiveOrExpression
    |   logicalAndExpression LogicalAnd inclusiveOrExpression
    ;

logicalOrExpression
    :   logicalAndExpression
    |   logicalOrExpression LogicalOr logicalAndExpression
    ;

conditionalExpression
    :   logicalOrExpression (Question expression Colon conditionalExpression)?
    ;

assignmentExpression
    :   conditionalExpression
    |   unaryExpression assignmentOperator assignmentExpression
    |   DigitSequence
    ;

assignmentOperator
    :   Assign | StarAssign | DivAssign | ModAssign | PlusAssign | MinusAssign
    |   LeftShiftAssign | RightShiftAssign | AndAssign | XorAssign | OrAssign
    ;

expression
    :   assignmentExpression
    |   expression Comma assignmentExpression
    ;

constantExpression
    :   conditionalExpression
    ;

declaration
    :   declarationSpecifiers initDeclaratorList Semi
	| 	declarationSpecifiers Semi
    ;

declarationSpecifiers
    :   declarationSpecifier+
    ;

declarationSpecifier
    :   storageClassSpecifier
    |   typeSpecifier
    |   typeQualifier
    |   functionSpecifier
    ;

initDeclaratorList
    :   initDeclarator
    |   initDeclaratorList Comma initDeclarator
    ;

initDeclarator
    :   declarator
    |   declarator Assign initializer
    ;

storageClassSpecifier
    :   Typedef
    |   Static
    |   Auto
    ;

typeSpecifier
    :   ( Void | Char | Short | Int | Long | Float | Double | Signed | Unsigned )
    |   structOrUnionSpecifier
    |   typedefName
    |   typeSpecifier pointer
    ;

structOrUnionSpecifier
    :   structOrUnion Identifier? LeftBrace structDeclarationList RightBrace
    |   structOrUnion Identifier
    ;

structOrUnion
    :   Struct | Union
    ;

structDeclarationList
    :   structDeclaration+
    ;

structDeclaration
    :   specifierQualifierList structDeclaratorList? Semi
    ;

specifierQualifierList
    :   typeSpecifier specifierQualifierList?
    |   typeQualifier specifierQualifierList?
    ;

structDeclaratorList
    :   structDeclarator
    |   structDeclaratorList Comma structDeclarator
    ;

structDeclarator
    :   declarator
    |   declarator? Colon constantExpression
    ;

typeQualifier
    :   Const | Restrict | Volatile
    ;

functionSpecifier
    :   Inline
    ;

declarator
    :   pointer? directDeclarator
    ;

directDeclarator
    :   Identifier
    |   LeftParen declarator RightParen
    |   directDeclarator LeftBracket typeQualifierList? assignmentExpression? RightBracket
    |   directDeclarator LeftBracket Static typeQualifierList? assignmentExpression RightBracket
    |   directDeclarator LeftBracket typeQualifierList Static assignmentExpression RightBracket
    |   directDeclarator LeftBracket typeQualifierList? Star RightBracket
    |   directDeclarator LeftParen parameterTypeList RightParen
    |   directDeclarator LeftParen identifierList? RightParen
    |   LeftParen typeSpecifier? pointer directDeclarator RightParen // function pointer like: (__cdecl *f)
    ;

nestedParenthesesBlock
    :   (   ~(LeftParen | RightParen)
        |   LeftParen nestedParenthesesBlock RightParen
        )*
    ;

pointer
    :   Star typeQualifierList?
    |   Star typeQualifierList? pointer
    ;

typeQualifierList
    :   typeQualifier+
    ;

parameterTypeList
    :   parameterList
    |   parameterList Comma Ellipsis
    ;

parameterList
    :   parameterDeclaration
    |   parameterList Comma parameterDeclaration
    ;

parameterDeclaration
    :   declarationSpecifiers declarator
    |   declarationSpecifiers
    ;

identifierList
    :   Identifier
    |   identifierList Comma Identifier
    ;

typeName
    :   specifierQualifierList
    ;

typedefName
    :   Identifier
    ;

initializer
    :   assignmentExpression
    |   LeftBrace initializerList RightBrace
    |   LeftBrace initializerList Comma RightBrace
    ;

initializerList
    :   designation? initializer
    |   initializerList Comma designation? initializer
    ;

designation
    :   designatorList Assign
    ;

designatorList
    :   designator+
    ;

designator
    :   LeftBracket constantExpression RightBracket
    |   Dot Identifier
    ;

statement
    :   labeledStatement
    |   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    ;

labeledStatement
    :   Identifier Colon statement
    |   Case constantExpression Colon statement
    |   Default Colon statement
    ;

compoundStatement
    :   LeftBrace blockItemList? RightBrace
    ;

blockItemList
    :   blockItem+
    ;

blockItem
    :   statement
    |   declaration
    ;

expressionStatement
    :   expression? Semi
    ;

selectionStatement
    :   If LeftParen expression RightParen statement (Else statement)?
    |   Switch LeftParen expression RightParen statement
    ;

iterationStatement
    :   While LeftParen expression RightParen statement
    |   Do statement While LeftParen expression RightParen Semi
    |   For LeftParen forCondition RightParen statement
    ;

forCondition
	:   forDeclaration Semi forExpression? Semi forExpression?
	|   expression? Semi forExpression? Semi forExpression?
	;

forDeclaration
    :   declarationSpecifiers initDeclaratorList?
    ;

forExpression
    :   assignmentExpression
    |   forExpression Comma assignmentExpression
    ;

jumpStatement
    :   Goto Identifier Semi
    |   Continue Semi
    |   Break Semi
    |   Return expression? Semi
    ;

compilationUnit
    :   externalDeclaration* EOF
    ;

externalDeclaration
    :   functionDefinition
    |   declaration
    |   Semi
    ;

functionDefinition
    :   declarationSpecifiers? declarator declarationList? compoundStatement
    ;

declarationList
    :   declaration+
    ;

// TOKENS

Auto : 'auto';
Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
Enum : 'enum';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Inline : 'inline';
Int : 'int';
Long : 'long';
Restrict : 'restrict';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Static : 'static';
Struct : 'struct';
Switch : 'switch';
Typedef : 'typedef';
Union : 'union';
Unsigned : 'unsigned';
Void : 'void';
Volatile : 'volatile';
While : 'while';

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LeftShift : '<<';
RightShift : '>>';

Plus : '+';
Increment : '++';
Minus : '-';
Descrement : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
LogicalAnd : '&&';
LogicalOr : '||';
Caret : '^';
Not : '!';
Tilde : '~';

Question : '?';
Colon : ':';
Semi : ';';
Comma : ',';

Assign : '=';
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';
LeftShiftAssign : '<<=';
RightShiftAssign : '>>=';
AndAssign : '&=';
XorAssign : '^=';
OrAssign : '|=';

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';
Ellipsis : '...';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    |   UniversalCharacterName
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

fragment
UniversalCharacterName
    :   '\\u' HexQuad
    |   '\\U' HexQuad HexQuad
    ;

fragment
HexQuad
    :   HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
    ;

Constant
    :   IntegerConstant
    |   FloatingConstant
    |   CharacterConstant
    ;

fragment
IntegerConstant
    :   DecimalConstant IntegerSuffix?
    |   OctalConstant IntegerSuffix?
    |   HexadecimalConstant IntegerSuffix?
    |	BinaryConstant
    ;

fragment
BinaryConstant
	:	'0' [bB] [0-1]+
	;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    ;

fragment
OctalConstant
    :   '0' OctalDigit*
    ;

fragment
HexadecimalConstant
    :   HexadecimalPrefix HexadecimalDigit+
    ;

fragment
HexadecimalPrefix
    :   '0' [xX]
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
OctalDigit
    :   [0-7]
    ;

fragment
HexadecimalDigit
    :   [0-9a-fA-F]
    ;

fragment
IntegerSuffix
    :   UnsignedSuffix LongSuffix?
    |   UnsignedSuffix LongLongSuffix
    |   LongSuffix UnsignedSuffix?
    |   LongLongSuffix UnsignedSuffix?
    ;

fragment
UnsignedSuffix
    :   [uU]
    ;

fragment
LongSuffix
    :   [lL]
    ;

fragment
LongLongSuffix
    :   'll' | 'LL'
    ;

fragment
FloatingConstant
    :   DecimalFloatingConstant
    |   HexadecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart? FloatingSuffix?
    |   DigitSequence ExponentPart FloatingSuffix?
    ;

fragment
HexadecimalFloatingConstant
    :   HexadecimalPrefix HexadecimalFractionalConstant BinaryExponentPart FloatingSuffix?
    |   HexadecimalPrefix HexadecimalDigitSequence BinaryExponentPart FloatingSuffix?
    ;

fragment
FractionalConstant
    :   DigitSequence? Dot DigitSequence
    |   DigitSequence Dot
    ;

fragment
ExponentPart
    :   'e' Sign? DigitSequence
    |   'E' Sign? DigitSequence
    ;

fragment
Sign
    :   '+' | '-'
    ;

DigitSequence
    :   Digit+
    ;

fragment
HexadecimalFractionalConstant
    :   HexadecimalDigitSequence? Dot HexadecimalDigitSequence
    |   HexadecimalDigitSequence Dot
    ;

fragment
BinaryExponentPart
    :   'p' Sign? DigitSequence
    |   'P' Sign? DigitSequence
    ;

fragment
HexadecimalDigitSequence
    :   HexadecimalDigit+
    ;

fragment
FloatingSuffix
    :   'f' | 'l' | 'F' | 'L'
    ;

fragment
CharacterConstant
    :   '\'' CCharSequence '\''
    |   'L\'' CCharSequence '\''
    |   'u\'' CCharSequence '\''
    |   'U\'' CCharSequence '\''
    ;

fragment
CCharSequence
    :   CChar+
    ;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
    ;

fragment
EscapeSequence
    :   SimpleEscapeSequence
    |   OctalEscapeSequence
    |   HexadecimalEscapeSequence
    |   UniversalCharacterName
    ;

fragment
SimpleEscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;

fragment
OctalEscapeSequence
    :   '\\' OctalDigit
    |   '\\' OctalDigit OctalDigit
    |   '\\' OctalDigit OctalDigit OctalDigit
    ;

fragment
HexadecimalEscapeSequence
    :   '\\x' HexadecimalDigit+
    ;

StringLiteral
    :   EncodingPrefix? '"' SCharSequence? '"'
    ;

fragment
EncodingPrefix
    :   'u8'
    |   'u'
    |   'U'
    |   'L'
    ;

fragment
SCharSequence
    :   SChar+
    ;

fragment
SChar
    :   ~["\\\r\n]
    |   EscapeSequence
    |   '\\\n'   // Added line
    |   '\\\r\n' // Added line
    ;

ComplexDefine
    :   '#' Whitespace? 'define'  ~[#]*
        -> skip
    ;

AsmBlock
    :   'asm' ~'{'* LeftBrace ~'}'* RightBrace
	    -> skip
    ;

LineAfterPreprocessing
    :   '#line' Whitespace* ~[\r\n]*
        -> skip
    ;

LineDirective
    :   '#' Whitespace? DecimalConstant Whitespace? StringLiteral ~[\r\n]*
        -> skip
    ;

PreprocessiorBlock
    : '#' ( 'include' | 'define' | If | 'elif' ) ~[\r\n]*
      -> skip
    ;

PragmaDirective
    :   '#' Whitespace? 'pragma' Whitespace ~[\r\n]*
        -> skip
    ;

Whitespace
    :   [ \t]+
        -> skip
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;