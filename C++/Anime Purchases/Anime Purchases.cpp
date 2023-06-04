#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <deque>

int main() {
    std::ifstream fileParam("large_params.txt");
    std::vector<double> market; //stock prices
    std::vector<int> list; // price list of anime titles
    std::vector<std::string> listLines; //list of things to buy with titles on it
	std::string line;
    std::stringstream sso;
    int nDays, kDays, mDays; 
    double priceParam;
    fileParam >> nDays >> kDays >> mDays;
    std::cout << nDays << '\n';
    std::cout << kDays << '\n';
    std::cout << mDays << '\n';
    while (fileParam >> priceParam) {
        market.push_back(priceParam);
    }
    std::ifstream filePurch("large_purchases.txt");
    while(getline(filePurch, line)) {
        listLines.push_back(line);
    }
    int sizePurch = listLines.size();
    for (int i = 0; i < sizePurch; ++i) { 
        std::string pricePurch, c;
        int listPrice = 0;
        int a = listLines[i].rfind(" ");
        int b = listLines[i].size();
        pricePurch = listLines[i];
        c = pricePurch.substr(a+1, b);
        sso << c;
        sso >> listPrice;
        list.push_back(listPrice);
        sso.clear();
    }
    std::vector<double> lowPrice;
    std::deque<double> storedPrices;
    int kDayCount = 1, mDayCount = 1, animeCount = 0;
    for (int i = 0; i < market.size(); i++) {
        int currentSize = storedPrices.size();
        if (currentSize == 0) { //If empty, store 1st item
            storedPrices.push_back(market[i]);
            mDayCount++;
            kDayCount++;
        }
        else if (mDayCount == mDays) { //If M days reached
            lowPrice.push_back(market[i]);
            storedPrices.clear();
            mDayCount = 1;
            kDayCount = 1;
            animeCount++;
        }
        else if (kDayCount>=kDays) { //If K days reached (lowest price for K days)
            if (market[i] < storedPrices[0]) {
                lowPrice.push_back(market[i]);
                mDayCount = 1;
                kDayCount = 1;
                animeCount++;
            }
            else if (kDayCount < mDays) {
                    mDayCount++;
                    kDayCount++;
                
            }
        }
        else if (kDayCount < kDays) {
            if (storedPrices[0] < market[i]) { //If price is still lowest
                kDayCount++;
                mDayCount++;
            }
            else { //If price is not lowest anymore
                storedPrices.clear();
                storedPrices.push_back(market[i]);
                kDayCount++;
                mDayCount++;
            }
        }
    }
    double sum = 0;
    for (int j = 0; j < lowPrice.size(); j++) {
        sum += (lowPrice[j]*list[j]);
    }
    //std::cout << "NUMBER OF ANIME PURCHASED: " <<animeCount << '\n';
    if (animeCount < list.size()) { //checks for remaining items not purchased
        int marketSize = market.size();
        for (int k = animeCount; k < list.size(); k++) {
            sum += market[marketSize-1]*list[k];
        }
    }
    std::cout << "Total expenses: " << sum << '\n';
    return 0;
}
  