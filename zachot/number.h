#ifndef NUMBER_H
#define NUMBER_H

#include <math.h>

class Number
{
public:
    Number();
    ~Number();

    double real;

    double getLength() { return real; }

    Number operator + (const Number& number);
    Number operator - (const Number& number);
    Number operator * (const Number& number);
    Number operator / (const Number& number);
    bool operator == (const Number& number);
    Number& operator = (const Number& number);
};

class ComplexNumber : public Number
{
public:
    ComplexNumber();
    ~ComplexNumber();

    double imaginary;

    double getLength() { return sqrt(real * real + imaginary * imaginary); }

    ComplexNumber operator + (const ComplexNumber& number);
    ComplexNumber operator - (const ComplexNumber& number);
    ComplexNumber operator * (const ComplexNumber& number);
    ComplexNumber operator / (const ComplexNumber& number);
    bool operator == (const ComplexNumber& number);
    ComplexNumber& operator = (const ComplexNumber& number);
};

#endif // NUMBER_H
