#include <iostream>
#include <string>
//Angel Omar Pardo Monreal
//Codigo de las clases de deporte y sub clases
// Quinto codigo 
//19/5/2025
 
using namespace std;


class Deporte {
public:
    string nombre;
    string tipoBalon;
    string duracion;          
    string lugar;          

    void mostrarInformacion() {
        cout << "Nombre del deporte: " << nombre << endl;
        cout << "Tipo de balon: " << tipoBalon << endl;
        cout << "Duracion del partido: " << duracion << " minutos" << endl;
        cout << "Lugar de juego: " << lugar << endl;
    }
};


class DeporteConManos : public Deporte {
public:
    int numeroJugadores;
    bool usaRed;
    bool usaProtecciones;
    string tipoDeGolpe;

    void mostrarCaracteristicas() {
        mostrarInformacion();
        cout << "Se juega con las manos" << endl;
        cout << "Numero de jugadores: " << numeroJugadores << endl;
        cout << "Usa red?: " << (usaRed ? "Si" : "No") << endl;
        cout << "Usa protecciones?: " << (usaProtecciones ? "Si" : "No") << endl;
        cout << "Tipo de golpe: " << tipoDeGolpe << endl;
    }
};


class DeporteConPies : public Deporte {
public:
    bool sePermiteCabecear;
    bool usaEspinilleras;
    int numeroJugadores;
    string tipoCalzado;
    int duracionMitad;

    void mostrarCaracteristicas() {
        mostrarInformacion();
        cout << "Se juega con los pies" << endl;
         cout << "Numero de jugadores: " << numeroJugadores << endl;
        cout << "Se permite cabecear?: " << (sePermiteCabecear ? "Si" : "No") << endl;
        cout << "Usa espinilleras?: " << (usaEspinilleras ? "Si" : "No") << endl;
        cout << "Tipo de calzado: " << tipoCalzado << endl;
        cout << "Duracion de cada mitad: " << duracionMitad << " minutos" << endl;
    }
};

int main() {
    
    DeporteConManos voleibol;
    voleibol.nombre = "Voleibol";
    voleibol.tipoBalon = "Balon de goma";
    voleibol.duracion = "60";
    voleibol.lugar = "Cancha cerrada";
    voleibol.numeroJugadores = 6;
    voleibol.usaRed = true;
    voleibol.usaProtecciones = true;
    voleibol.tipoDeGolpe = "Remate";

    DeporteConPies futbol;
    futbol.nombre = "Futbol";
    futbol.tipoBalon = "Balon de soccer de numero 8";
    futbol.duracion = "2 tiempos de 45 minutos y tiempo extra";
    futbol.numeroJugadores = 6;
    futbol.lugar = "Aire libre";
    futbol.sePermiteCabecear = true;
    futbol.usaEspinilleras = true;
    futbol.tipoCalzado = "Tacohones";
    futbol.duracionMitad = 45;

    cout << "=== Deporte con manos ===" << endl;
    voleibol.mostrarCaracteristicas();

    cout << "\n=== Deporte con pies ===" << endl;
    futbol.mostrarCaracteristicas();

    return 0;
}
//Lerr una cadena y diga en que estado se queda 
