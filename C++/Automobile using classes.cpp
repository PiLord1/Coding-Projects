#include <iostream>
#include <string>
#include <iomanip>

class Automobile {
    private:
        double v;
        bool is_KPH;
        int *space;
    public:
        static int count;
        Automobile(double v);
        Automobile();
        ~Automobile();
        void setV(const double new_v);
        double getV();
        void toMPS();
};

int Automobile::count = 0;

Automobile::Automobile():v(60), is_KPH(true)  {
  this -> space = new int[1000];
  std::cout << "Default constructor invoked" << '\n';
  Automobile::count++;
  std::cout << "Current no. of constructors: " << count << '\n';
}

Automobile::Automobile(double v){
  this -> space = new int[1000];
  this -> v = v;
  std::cout << "Normal constructor invoked" << '\n';
  Automobile::count++;
  std::cout << "Current no. of constructors: " << count << '\n';
}

Automobile::~Automobile() {
  Automobile::count--;
  std::cout << "Destroying..." << count << '\n';
  delete[] this -> space;
}

void Automobile::setV(const double new_v){
    this -> v = new_v;
    std::cout << "The new velocity is " << new_v << "." << '\n';
}

double Automobile::getV(){
    return this -> v;
}

double getFasterAutomobile(double v1, double v2){
    return (v1 < v2 ? v2 : v1);
}

void Automobile::toMPS(){
    this -> v = (v*1000)/3600;
    this -> is_KPH = false;
}

int main(){
  double v2, v3, v4, v5;
  Automobile A1(100);
  std::cout << "Enter velocity of Automobile 2: ";
  std::cin >> v2;
  std::cout << '\n';
  Automobile A2(v2);
  std::cout << "Enter velocity of Automobile 3: ";
  std::cin >> v3;
  std::cout << '\n';
  Automobile A3(v3);
  std::cout << "Enter velocity of Automobile 4: ";
  std::cin >> v4;
  std::cout << '\n';
  Automobile A4(v4);
  std::cout << "Enter velocity of Automobile 5: ";
  std::cin >> v5;
  std::cout << '\n';
  Automobile A5(v5);
  A1.toMPS();
  A2.toMPS();
  A3.toMPS();
  A4.toMPS();
  A5.toMPS();
  std::cout << "Automobile 1 has a velocity of " << A1.getV() << " m/s." << '\n';
  std::cout << "Automobile 2 has a velocity of " << A2.getV() << " m/s." << '\n';
  std::cout << "Automobile 3 has a velocity of " << A3.getV() << " m/s." << '\n';
  std::cout << "Automobile 4 has a velocity of " << A4.getV() << " m/s." << '\n';
  std::cout << "Automobile 5 has a velocity of " << A5.getV() << " m/s." << '\n';
  std::cout << '\n';
  std::cout << getFasterAutomobile(A1.getV(),A2.getV()) << " m/s" << '\n';
  std::cout << getFasterAutomobile(A2.getV(),A3.getV()) << " m/s" << '\n';
  std::cout << getFasterAutomobile(A3.getV(),A4.getV()) << " m/s" << '\n';
  std::cout << getFasterAutomobile(A4.getV(),A5.getV()) << " m/s" << '\n';
  std::cout << '\n';
  return 0;
}