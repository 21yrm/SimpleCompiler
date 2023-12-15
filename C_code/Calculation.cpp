void *memset(void *s, int ch, size_t n);
size_t strlen(const char *_Str);
int printf( const char *restrict format, ... );
int scanf(const char *__format, ...);

char opStack[8192];
float numStack[8192];
int opIndex = -1;
int numIndex = -1;

char orderBetween(char a, char b){
    if(opIndex == -1)
        return '>';
    switch (a)
    {
        case '*':
        case '/':
            if(b == '*' || b == '/')
                return '<';
            else
                return '>';
        case '+':
        case '-':
            if(b == '(')
                return '>';
            return '<';
    }
}

void popOpStack(){
    switch (opStack[opIndex])
    {
        case '+':
            numStack[numIndex - 1] = numStack[numIndex - 1] + numStack[numIndex];
            break;
        case '-':
            numStack[numIndex - 1] = numStack[numIndex - 1] - numStack[numIndex];
            break;
        case '*':
            numStack[numIndex - 1] = numStack[numIndex - 1] * numStack[numIndex];
            break;
        case '/':
            numStack[numIndex - 1] = numStack[numIndex - 1] / numStack[numIndex];
            break;
    }
    numIndex--;
    opIndex--;
    return;
}

int evaluate(char* equation){
    bool lastDigit = false;
    memset(opStack, 8192, ' ');
    memset(numStack, 8192, 0);
    for(int i = 0; i < strlen(equation); i++){
        if(equation[i] == '('){
            opStack[++opIndex] = '(';
            lastDigit = false;
        }
        else if(equation[i] == ')'){
            while(opStack[opIndex] != '(')
                popOpStack();
            opIndex--;
            lastDigit = false;
        }
        else if(equation[i] >= '0' && equation[i] <= '9'){
            if(lastDigit){
                numStack[numIndex] *= 10;
                numStack[numIndex] += equation[i] - '0';
            }
            else{
                lastDigit = true;
                numStack[++numIndex] = equation[i] - '0';
            }
        }
        else{
            if(orderBetween(equation[i], opStack[opIndex]) == '<')
                popOpStack();
            opStack[++opIndex] = equation[i];
            lastDigit = false;
        }
    }
    while (opIndex != -1)
    {
        popOpStack();
    }
    return numStack[0];
}

void modify(char* src, char* tar){
    int i = 0, j = 0;
    for(; i < strlen(src); ){
        if(src[i] == '-' && !(src[i - 1] > '0' && src[i - 1] < '9'))
            tar[j++] = '0';
        tar[j++] = src[i++];
    }
}

int main(){
    char equation[8192];
    char modifiedEquation[8192];
    scanf("%s", &equation);
    modify(equation, modifiedEquation);
    printf("The result of the equation is %d", evaluate(modifiedEquation));
    return 0;
}