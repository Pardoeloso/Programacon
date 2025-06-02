#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream archivo("Diego.txt"); 

    if (!archivo.is_open()) {
        cerr << "No se pudo abrir el archivo 'Diego.txt'" << endl;
        return 1;
    }

    string linea;
    cout << "Contenido del archivo 'Diego.txt':\n\n";

    while (getline(archivo, linea)) {
        cout << linea << endl;
    }

    archivo.close();
    return 0;
}

