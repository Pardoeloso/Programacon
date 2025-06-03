#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main() 
{
    std::ifstream archivo("Diego.txt");  // Abre el archivo
    std::stringstream buffer;
    std::string contenido;

    if (archivo) 
    {
        buffer << archivo.rdbuf();        // Copia contenido en buffer
        contenido = buffer.str();         // Convierte a string

        std::cout << "Este es el contenido del archivo:\n";
        std::cout << contenido << std::endl;
    } 
    else 
    {
        std::cerr << "No se encontró el archivo." << std::endl;
    }

    return 0;
}

