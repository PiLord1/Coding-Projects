#include <iostream>
#include <string>
#include <limits>
#include <iomanip>
#include <vector>
#include <cmath>

class Evector {
    private:
    unsigned int length;
    int *space;

    public:
    std::vector<double> finalVect;
    Evector();
    Evector(std::vector<double> inputVect);
    Evector(std::vector<double> inputVect, int length_vect);
    Evector(const Evector &E1);
    void operator=(const Evector &E1);
    Evector operator+(const Evector &E1);
    Evector operator-(const Evector &E1);
    friend Evector operator*(const Evector &E1, const double scalar); 
    friend Evector operator*(const double scalar, const Evector &E1);
    double operator*(const Evector &E1);
    double& operator[](int i);
    double mag();
    double getElement(int index);
    void setElement(int index, double value);
};

Evector::Evector() {
    std::vector<double> vectOutput;
    this -> space = new int[1000];
    vectOutput.push_back(0.0);
    finalVect = vectOutput;
    std::cout << "Default constructor invoked" << '\n';
}

Evector::Evector(std::vector<double> inputVect) {
    std::vector<double> vectOutput;
    this -> space = new int[1000];
    int vectSize = inputVect.size();
    std::cout << "Regular constructor invoked" << '\n';
    for (int i = 0; i < vectSize; ++i) {
        vectOutput.push_back(inputVect[i]);
    }
    finalVect = vectOutput;
}

Evector::Evector(std::vector<double> inputVect, int length_vect)  { //changed length to length_vect
    std::vector<double> vectOutput;
    this -> space = new int[1000];
    this -> length = length_vect;
    int vectSize1 = inputVect.size();
    std::cout << "Regular constructor invoked" << '\n';
    if (vectSize1 < length_vect) {
        int missing = length_vect - vectSize1;
        for (int i = 0; i < missing; ++i) {
            inputVect.push_back(0.0);
        }
        int vectSize2 = inputVect.size();
        for (int j = 0; j < vectSize2; ++j) {
            vectOutput.push_back(inputVect[j]);
            finalVect = vectOutput;
        }
    } 
    else {
        std::cout << "Default constructor invoked" << '\n';
        vectOutput.push_back(0.0);
        finalVect = vectOutput;
    }
}

Evector::Evector(const Evector &E1) {
    this -> space = new int[1000];
    std::vector<double> vectOutput;
    int vectSize = E1.finalVect.size();
    for (int i = 0; i < vectSize; ++i) {
        vectOutput.push_back(E1.finalVect[i]);
    }
    finalVect = vectOutput;
    std::cout << "Copy constructor invoked" << '\n';
}

void Evector::operator=(const Evector &E1) {
    this -> space = new int[1000];
    std::vector<double> vectOutput;
    int vectSize = E1.finalVect.size();
    for (int i = 0; i < vectSize; ++i) {
        vectOutput.push_back(E1.finalVect[i]);
    }
    finalVect = vectOutput;
    std::cout << "Equal sign done overloading" << '\n';
}

Evector Evector::operator+(const Evector &E1) {
    std::vector <double> vectOutput;
    std::vector <double> vectReturn;
    int vectSize1 = E1.finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    finalVect = vectOutput;
    int vectSize2 = vectOutput.size();
    if (vectSize1 != vectSize2) {
        double null = 0.0;
        vectReturn.push_back(null);
        std::cout << "Addition sign done overloading\nError: Vectors can't be added" << '\n';
    } 
    else {
        for (int j = 0; j < vectSize1; ++j) {
            vectReturn.push_back(double(finalVect[j]) + double(E1.finalVect[j]));
        }
        std::cout << "Addition sign done overloading\nAdding successful!" << '\n';
    }
    return Evector (vectReturn);
}

Evector Evector::operator-(const Evector &E1) {
    std::vector <double> vectOutput;
    std::vector <double> vectReturn;
    int vectSize1 = E1.finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    this -> finalVect = vectOutput;
    int vectSize2 = vectOutput.size();
    if (vectSize1 != vectSize2) {
        double null = 0.0;
        vectReturn.push_back(null);
        std::cout << "Subtraction sign done overloading\nError: Vectors can't be subtracted" << '\n';
    } 
    else {
        for (int j = 0; j < vectSize1; ++j) {
            vectReturn.push_back(double(finalVect[j]) - double(E1.finalVect[j]));
        }
        std::cout << "Subtraction sign done overloading\nSubtracting successful!" << '\n';
    }
    return Evector (vectReturn);
}

Evector operator*(const Evector &E1, const double scalar) {
    std::vector<double> vectReturn;
    std::cout << "Product sign done overloading\nEvector * scalar successful!" << '\n';
    int vectSize = E1.finalVect.size();
    for (int j = 0; j < vectSize; ++j) {
        vectReturn.push_back(double(E1.finalVect[j]) * scalar);
    }
    return Evector (vectReturn);
}

Evector operator*(const double scalar, const Evector &E1) {
    std::vector<double> vectReturn;
    std::cout << "Product sign done overloading\nscalar * Evector successful!" << '\n';
    int vectSize = E1.finalVect.size();
    for(int i = 0; i < vectSize; ++i) {
        vectReturn.push_back(scalar * double(E1.finalVect[i]));
    }
    return Evector (vectReturn);
}

double Evector::operator*(const Evector &E1) {
    std::vector <double> vectOutput;
    std::vector <double> vectReturn;
    double add = 0;
    int vectSize1 = E1.finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    finalVect = finalVect;
    int vectSize2 = vectOutput.size();
    if (vectSize1 != vectSize2) {
        std::cout << "Product sign done overloading\nError: Vectors can't be multiplied";
        double infinite = -1.0*1780000000000000000000000000000000000.0;
        return infinite; 
    }
    else {
        for (int j = 0; j < vectSize1; ++j) {
            double dotProd = finalVect[j] * E1.finalVect[j];
            add += dotProd;
        }
        std::cout << "Product sign done overloading\nEvector * Evector successful!" << '\n';
        return add;
    }
}

double& Evector::operator[](int locate) {
    std::vector<double> vectOutput;
    int vectSize1 = finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    finalVect = vectOutput;
    int vectSize = vectOutput.size();
    int indexSize = vectSize - 1;
    if (indexSize < locate || locate < 0) {
        std::cout << "Error: input index invalid" << '\n';
        double *a = 0;
        return *a;
    }
    else {
        std::cout << "Bracket operator successful!" << '\n';
        std::cout << "Value acquired successfully!" << '\n';
        return vectOutput[locate];
    }
}

double Evector::getElement(int index) {
    std::vector<double> vectOutput;
    int vectSize1 = finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    finalVect = vectOutput;
    double getIndex;
    int vectSize = vectOutput.size();
    int indexSize = vectSize - 1;
    if (indexSize < index || index < 0) {
        std::cout << "Error: input index invalid" << '\n';
    }
    else {
        std::cout << "Value acquired successfully!" << '\n';
        getIndex = vectOutput[index];
        return getIndex;
    }
    return 0;
}

void Evector::setElement(int index, double value) {
    std::vector<double> vectOutput;
    int vectSize1 = finalVect.size();
    for (int i = 0; i < vectSize1; ++i) {
        vectOutput.push_back(finalVect[i]);
    }
    finalVect = vectOutput;
    int vectSize = vectOutput.size();
    int indexSize = vectSize - 1;
    if (indexSize < index || index < 0) {
        std::cout << "Error: input index invalid" << '\n';
    }
    else {
        std::cout << "Value changed successfully!" << '\n';
        vectOutput[index] = value;
    }
}

double Evector::mag() {
    double sum = 0;
    finalVect = finalVect;
    int vectSize = finalVect.size();
    for (int i = 0; i < vectSize; ++i) {
        double square = finalVect[i]*finalVect[i];
        sum += square;
    }
    std::cout << "Magnitude successfully calculated!" << '\n';
    return sqrt(sum);
}





