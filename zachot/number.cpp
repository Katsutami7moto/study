#include "number.h"

// Вещественные числа

Number::Number()
{
    real = 0;
}

Number::~Number()
{
}

Number Number::operator + (const Number& number)
{
    Number _number;
    _number.real = real + number.real;
    return _number;
}

Number Number::operator - (const Number& number)
{
    Number _number;
    _number.real = real - number.real;
    return _number;
}

Number Number::operator * (const Number& number)
{
    Number _number;
    _number.real = real * number.real;
    return _number;
}

Number Number::operator / (const Number& number)
{
    Number _number;
    _number.real = real / number.real;
    return _number;
}

bool Number::operator == (const Number& number)
{
    return real == number.real;
}

Number& Number::operator = (const Number& number)
{
    real = number.real;

    return *this;
}

// Комплексные числа

ComplexNumber::ComplexNumber()
{
    imaginary = 0;
}

ComplexNumber::~ComplexNumber()
{
}

ComplexNumber ComplexNumber::operator + (const ComplexNumber& complex)
{
    ComplexNumber _complex;
    _complex.real = real + complex.real;
    _complex.imaginary = imaginary + complex.imaginary;
    return _complex;
}

ComplexNumber ComplexNumber::operator - (const ComplexNumber& complex)
{
    ComplexNumber _complex;
    _complex.real = real - complex.real;
    _complex.imaginary = imaginary - complex.imaginary;
    return _complex;
}

ComplexNumber ComplexNumber::operator * (const ComplexNumber& complex)
{
    ComplexNumber _complex;
    _complex.real = real * complex.real - imaginary * complex.imaginary;
    _complex.imaginary = real * complex.imaginary + imaginary * complex.real;
    return _complex;
}

ComplexNumber ComplexNumber::operator / (const ComplexNumber& complex)
{
    ComplexNumber _complex;
    _complex.real = (real * complex.real + imaginary * complex.imaginary) /
            (complex.real * complex.real + complex.imaginary * complex.imaginary);
    _complex.imaginary = (imaginary * complex.real - real * complex.imaginary) /
            (complex.real * complex.real + complex.imaginary * complex.imaginary);
    return _complex;
}

bool ComplexNumber::operator == (const ComplexNumber& complex)
{
    return real == complex.real && imaginary == complex.imaginary;
}

ComplexNumber& ComplexNumber::operator = (const ComplexNumber& complex)
{
    real = complex.real;
    imaginary = complex.imaginary;

    return *this;
}
