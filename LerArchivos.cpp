#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
//Angel Omar Pardo Monreal
//Decimo codigo
//Hacer que se lea un archivo txt
//14/29/2025
int main() 
{
    std::ifstream archivo("Diego.txt");  
    std::stringstream buffer;
    std::string contenido;

    if (archivo) 
    {
        buffer << archivo.rdbuf();        
        contenido = buffer.str();         

        std::cout << "Este es el contenido del archivo:\n";
        std::cout << contenido << std::endl;
    } 
    else 
    {
        std::cerr << "No se encontró el archivo." << std::endl;
    }

    return 0;
}

