#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

unsigned int count_words(const std::string& input)
{
        std::stringstream ss(input);
        std::string word;

        unsigned int ctr = 0;
        while (ss >> word)
                ctr++;
        return ctr;
}

int main()
{
	std::fstream mydata("names.txt");
	std::vector <std::string> croom;
	std::string student;
	int nlines = 6, sum = 0;
	for (int i = 0; i < nlines; i++)
	{
		getline(mydata, student);
		croom.push_back(student);
	}
	for (int i = 0; i < nlines; i++)
	{
		int printer = count_words(croom[i]);
        std::string score;
		std::stringstream line;
		std::string name;
		for (int j = 0; j < printer; ++j)
		{
			if (j < printer-1)
			{
				line << croom[i];
				line >> name;
				std::cout << name << " ";
			}
			else
			{
				line << croom[i];
				int score = 0;
				line >> score;
				std::cout << "has scored " << score << '\n';
				sum += score;
			}
		}
	}
	double average = double(sum) / double(nlines);
	std::cout << "Average: " << average << '\n';
	return 0;
}