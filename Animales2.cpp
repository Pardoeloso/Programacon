#include <iostream>
//Angel Omar Pardo Monreal
//Cuarto codigo 
// Crear Clases y objetos de animales
//14/04/2025
using namespace std;
class Animal{
public:
string color;
string tipo;
void MostrarInformacion(){
	cout<<"color: " << color << endl;
	cout<<"tipo: " << tipo << endl;
 }
};
class invertebrados: public Animal {
	public:
		bool tieneExoesqueleto;
        string TipoCuerpo;
         MostrarCaracteristicas();
          MostraInformacion();
           cout<<"esqueleto: " << esqueleto << endl;
   }
};
class vertebrados: public Animal{
	public:
		string Noesqueleto;
		  MostrarCaracteristicas()
           MostraInformacion();
            cout<<"Noesqueleto: " << Noesqueleto << endl;
};
int main()
{
	vertebrados leon
	leon.nombre = "Leon";
	leon.tipo = "Vertebrado";
	leon.esqueleto ="Oseo";
	
	Invertebrado pulpo;
	pulpo.nombre = "Pulpo";
	pulpo.tipo = "Invertebrado";
	pulpo.tipoCuerpo = "Blandos sin coulumna";
	pulpo.tieneExoesqueleto = false;
	
	count<<"=== Animal Vertebrado ==="<< endl;
	leon.mostrarCaracteristicas();
	cout<<"\n=== Animal invertebrado ===" << endl;
	pulpo.mostrarCaracteristicas();
		



return 0;
}

	
