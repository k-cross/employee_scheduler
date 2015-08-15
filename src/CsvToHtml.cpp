// CsvToHtml.cpp : This is formatter for the .csv Scheduler output. 
// It parses the standard .csv output or R to a nicer looking .html file
//
// Two commands are taken by the tool, 1.) .csv file & 2.) desired output .html file
//
#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[]){

	if (argc != 3){
		cout << argc << endl;
		cout << "this tool only takes two arguements source path (.csv) and destination path (.html)" << endl;
		return 0;
	}

	bool first_row, f_alt;

	ifstream ifile;
	ifile.open(argv[1]);
	if (ifile.fail())
		cout << "ifile failed to open!" << endl;

	ofstream ofile;
	ofile.open(argv[2]);
	if (!ifile.good())
		cout << "ifile failed to open!" << endl;

	// Preformatting
	ofile << "<!DOCTYPE html> <html> <head> <style> h1{ font-family: Helvetica, sans-serif; } caption{ background-color: #96B53B; color: #000000; } #employee { font-family: \"Trebuchet MS\", Arial, Helvetica, sans-serif; width: 100%; border-collapse: collapse; } #employee td, #employee th { font-size: 1em; border: 1px solid #98bf21; padding: 3px 7px 2px 7px; } #employee th { font-size: 1.1em; text-align: left; padding-top: 5px; padding-bottom: 4px; background-color: #A7C942; color: #ffffff; } #employee tr.alt td { color: #000000; background-color: #EAF2D3; } </style> </head> <body> " << endl;
	ofile << "<table id=\"employee\"> \n<caption><h1>Employee Weekly Schedule</h1></caption> \n<tr> <th> </th>";

	// get first 2 char and dispose (blank data)
	for (int i = 0; i < 2; i++)
		ifile.get();

	char next;

	first_row = true;
	f_alt = false;

	while (ifile.good()){

		next = ifile.get();

		// make an entry <td>
		if (next == ',' && ifile.peek() == '"'){
			ifile.get();

			if (first_row)
				ofile << "<th>";
			else 
				ofile << "<td>";

			while (ifile.peek() != '"'){
				next = ifile.get();
				ofile << next;
			}
			ifile.get();

			if (first_row)
				ofile << "</th> ";
			else
				ofile << "</td> ";
		}

		// make a new row <tr>
		else if (next == '"'){
			first_row = false;

			ofile << "</tr>\n" << endl;

			if (f_alt)
				ofile << "<tr class=\"alt\"> ";
			else
				ofile << "<tr> ";
			ofile << "<th>";
			while (ifile.peek() != '"'){
				next = ifile.get();
				ofile << next;
			}
			ifile.get();
			ofile << "</th> ";

			f_alt = !f_alt;
		}
	}
	ifile.close();

	// Postformatting
	ofile << "</tr> \n</table> \n</body> \n</html>" << endl;

	ofile.close();

	cout << "Conversion complete!" << endl;
	return 0;
}

