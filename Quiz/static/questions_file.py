class questions_file:
    c_data = [
    [
    "1. Who is the father of C language?",
    "a. Bjarne Stroustrup ",
    "b. James A. Gosling",
    "c. Dennis Ritchie",
    "d. Dr. E.F. Codd"
    ],
    [
    "2. Which of the following is not a valid variable name declaration?",
    "a. int _a3",
    "b. int a_3",
    "c. int 3_a",
    "d. int _3a"
    ],
    [
    "3. Which data type is most suitable for storing a number 65000 in a 32-bit system?",
    "a. signed short",
    "b. unsigned short",
    "c. long",
    "d. int"
    ],
    [
    "4. enum types are processed by ___",
    "a. Compiler",
    "b. Preprocessor",
    "c. Linker",
    "d. Assembler"
    ],
    [
    "5. What is the precedence of arithmetic operators (from highest to lowest)?",
    "a. %, *, /, +, –",
    "b. %, +, /, *, –",
    "c. +, -, %, *, /",
    "d. %, +, -, *, /"
    ],
    [
    "6. What is the result of logical or relational expression in C?",
    "a. True or False",
    "b. 0 or 1",
    "c. 0 if an expression is false and any positive number if an expression is true",
    "d. None of the above"
    ],
    [
    "7. Which of the following is a correct format for declaration of function?",
    "a. return-type function-name(argument type);",
    "b. return-type function-name(argument type){}",
    "c. return-type (argument type)function-name;",
    "d. All of the above"
    ],
    [
    "8. Which of the following is true for the static variable?",
    "a. It can be called from another function",
    "b. It exists even after the function ends",
    "c. It can be modified in another function by sending it as a parameter",
    "d. All of the above"
    ],
    [
    "9. Which of the following is the correct syntax to send an array as a parameter to function?",
    "a. func(&array);",
    "b. func(#array);",
    "c. func(*array);",
    "d. func(array[size]);"
    ],
    [
    "10. Which of the following cannot be a structure member?",
    "a. Another structure",
    "b. Function",
    "c. Array",
    "d. String"
    ]
    ];

    c_answers = ["3","3","2","1","1","2","1","2","1","2"]


    cpp_data = [
    [
    "1. Who is the father of C++ language?",
    "a. Bjarne Stroustrup ",
    "b. James A. Gosling",
    "c. Dennis Ritchie",
    "d. Dr. E.F. Codd"
    ],
    [
    "2. What are the formal parameters in C++? ",
    "a. Parameters with which functions are called",
    "b. Parameters which are used in the definition of the function",
    "c. Variables other than passed parameters in a function",
    "d. Variables that are never used in the function"
    ],
    [
    "3. Which of the following is FALSE about references in C++ ",
    "a. References cannot be NULL",
    "b. A reference must be initialized when declared",
    "c. Once a reference is created, it cannot be later made to reference another object; it cannot be reset.",
    "d. References cannot refer to constant value"
    ],
    [
    "4. One of the following is true for an inline function.",
    "a. It executes faster as it is treated as a macro internally",
    "b. It doesn’t executes faster compared to a normal function ",
    "c. It executes faster because it priority is more than normal function ",
    "d. None of the above holds true for an inline function "
    ],
    [
    "5. Runtime polymorphism is done using.",
    "a. Function overloading",
    "b. Virtual classes",
    "c. Virtual functions",
    "d. Friend function"
    ],
    [
    "6.  Objects created using new operator are stored in __ memory.",
    "a. Cache",
    "b. Heap",
    "c. Stack",
    "d. Main"			
    ],
    [
    "7. Which of the following is called address operator?",
    "a. *",
    "b. &",
    "c. _",
    "d. %"
    ],
    [
    "8. How a reference is different from a pointer",
    "a. A reference cannot be null",
    "b. A reference once established cannot be changed",
    "c. The reference doesn’t need an explicit dereferencing mechanism",
    "d. All of the above"
    ],
    [
    "9. The data elements in the structure are also known as what?",
    "a. objects",
    "b. members",
    "c. data",
    "d. objects and data"
    ],
    [
    "10. Which of the following accesses a variable in structure *b?",
    "a. b->var;",
    "b. b.var;",
    "c. b>var;",
    "d. b-var;"
    ]
    ];

    cpp_answers = ["4","1","3","3","2","2","1","4","3","2"]


    java_data = [
    [
    "1. Who is the father of Java language?",
    "a. Bjarne Stroustrup ",
    "b. James Gosling",
    "c. Dennis Ritchie",
    "d. Dr. E.F. Codd"
    ],
    [
    "2. Which data type value is returned by all transcendental math functions?",
    "a. int",
    "b. float",
    "c. double",
    "d. long"
    ],
    [
    "3. Which of these can not be used for a variable name in Java? ",
    "a. identifier",
    "b. keyword",
    "c. identifier & keyword",
    "d. None of the above"
    ],
    [
    "4. What is the prototype of the default constructor of this Java class? \n     public class prototype { }",
    "a. prototype()",
    "b. prototype(void)",
    "c. public prototype(void)",
    "d. public prototype()"
    ],
    [
    "5. Which of these is an incorrect Statement?",
    "a. It is necessary to use new operator to initialize an array",
    "b. Array can be initialized using comma separated expressions surrounded by curly braces",
    "c. Array can be initialized when they are declared",
    "d. None of the above"
    ],
    [
    "6. Which of these is a process of converting a simple data type into a class?",
    "a. type wrapping",
    "b. type conversion",
    "c. type casting",
    "d. None of the above"
    ],
    [
    "7. Which of the below is invalid identifier with the main method?",
    "a. public",
    "b. static",
    "c. private",
    "d. final"
    ],
    [
    "8. What is the extension of compiled java classes?",
    "a. .class",
    "b. .java",
    "c. .txt",
    "d. .js"
    ],
    [
    "9. If a class inheriting an abstract class does not define all of its function then it will be known as?",
    "a. Abstract",
    "b. A simple class",
    "c. Static class",
    "d. Public class"
    ],
    [
    "10. Which of these packages contain all the Java’s built in exceptions?",
    "a. java.io",
    "b. java.util",
    "c. java.lang",
    "d. java.net"
    ]
    ];

    java_answers = ["2","3","2","4","1","1","3","1","1","3"]


    py_data = [
    [
    "1. Which of these is not a core data type?",
    "a. List",
    "b. Dictionary",
    "c. Tuples",
    "d. Class"
    ],
    [
    "2. What data type is the object below ? \n L = [1, 23, ‘hello’, 1]",
    "a. List",
    "b. Dictionary",
    "c. Tuple",
    "d. Array"
    ],
    [
    "3. Which of the following function convert a string to a float in python?",
    "a. int(x [,base] )",
    "b. long(x [,base] )",
    "c. float(x)",
    "d. str(x)"
    ],
    [
    "4. What is the output of the expression : 3*1**3",
    "a. 27",
    "b. 9",
    "c. 3",
    "d. 1"
    ],
    [
    "5. What is the output of the following program : \n print 'abcefd'.replace('cd', '12')",
    "a. ab1ef2",
    "b. abcefd",
    "c. ab1efd",
    "d. ab12ed2"
    ],
    [
    "6. What will be the output of the following code :\n  print type(type(int))",
    "a. type 'int'",
    "b. type 'type'",
    "c. Error",
    "d. 0"			
    ],
    [
    "7. What is the output of the following program :\n  y = 8 \n z = lambda x : x * y \n print z(6)",
    "a. 48",
    "b. 14",
    "c. 64",
    "d. None of the above"
    ],
    [
    "8. What is called when a function is defined inside a class?",
    "a. Module",
    "b. Class",
    "c. Another Function",
    "d. Method"
    ],
    [
    "9. Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?",
    "a. [3, 4, 5, 20, 5, 25, 1, 3]",
    "b. [1, 3, 3, 4, 5, 5, 20, 25]",
    "c. [3, 5, 20, 5, 25, 1, 3]",
    "d. [1, 3, 4, 5, 20, 5, 25]"
    ],
    [
    "10. Which operator is overloaded by the or() function?",
    "a. ||",
    "b. |",
    "c. //",
    "d. /"
    ]
    ];

    py_answers = ["4","1","3","3","2","2","1","4","3","2"]


    js_data = [
    [
    "1. Which is not JavaScript keyword? ",
    "a. int",
    "b. var",
    "c. let",
    "d. const"
    ],
    [
    "2. In which HTML element do we put in JavaScript code?",
    "a. &lt;js&gt;",
    "b. &lt;script&gt;",
    "c. &lt;body&gt;",
    "d. &lt;javascript&gt;"
    ],
    [
    "3. A variable in JavaScript must start with which special character?",
    "a. @",
    "b. $",
    "c. #",
    "d. No special character"
    ],
    [
    "4. What is the syntax for creating a function in JavaScript named as jsFunc?",
    "a. function = jsFunc()",
    "b. function jsFunc()",
    "c. function := jsFunc()",
    "d. function : jsFunc()"
    ],
    [
    "5. How is the function called in JavaScript named as jsFunc?",
    "a. call jsFunc();",
    "b. call function jsFunc();",
    "c. jsFunc();",
    "d. function jsFunc();"
    ],
    [
    "6. How would you write \"Hello\" in an alert box?",
    "a. msg(\"Hello\");",
    "b. alertBox(\"Hello\");",
    "c. document.write(\"Hello\");",
    "d. alert(\"Hello\")"			
    ],
    [
    "7. Which HTML attribute is used to reference an external JavaScript file?",
    "a. src",
    "b. rel",
    "c. type",
    "d. href"
    ],
    [
    "8. The setTimeout() belongs to which object?",
    "a. Element",
    "b. Window",
    "c. Location",
    "d. Event"
    ],
    [
    "9. Which of the following is not a reserved word in JavaScript?",
    "a. interface",
    "b. throws",
    "c. program",
    "d. short"
    ],
    [
    "10. What is the JavaScript syntax for printing values in Console?",
    "a. print(5);",
    "b. console.log(5);",
    "c. console.print(5);",
    "d. print.console(5);"
    ]
    ];

    js_answers = ["1","2","4","2","3","4","1","2","3","2"]