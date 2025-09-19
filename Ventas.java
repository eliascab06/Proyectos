import java.util.Scanner;

public class Ventas {
    static int[][] ventas = new int[12][3]; 
    static String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    // Insertar venta
    public static void insertarVenta(int mes, int depto, int valor) {
        ventas[mes][depto] = valor;
    }

    // Buscar venta
    public static int buscarVenta(int mes, int depto) {
        return ventas[mes][depto];
    }

    // Eliminar venta
    public static void eliminarVenta(int mes, int depto) {
        ventas[mes][depto] = 0;
    }

    // Mostrar todas las ventas
    public static void mostrarVentas() {
        System.out.println("\nTabla de Ventas:");
        System.out.printf("%12s %12s %12s %12s\n", "Mes", "Ropa", "Deportes", "Juguetería");
        for (int i = 0; i < ventas.length; i++) {
            System.out.printf("%12s", meses[i]);
            for (int j = 0; j < ventas[i].length; j++) {
                System.out.printf("%12d", ventas[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Captura de ventas por teclado
        for (int i = 0; i < meses.length; i++) {
            System.out.println("\n--- Ingresar ventas para " + meses[i] + " ---");
            for (int j = 0; j < departamentos.length; j++) {
                System.out.print("Ingrese ventas en " + departamentos[j] + ": ");
                int valor = sc.nextInt();
                insertarVenta(i, j, valor);
            }
        }

        // Mostrar tabla completa
        mostrarVentas();

        // Ejemplo de búsqueda
        System.out.println("\nBuscar ventas de Julio en Deportes:");
        System.out.println("Ventas encontradas: " + buscarVenta(6, 1)); // Julio - Deportes

        // Ejemplo de eliminación
        System.out.println("\nEliminando ventas de Enero en Ropa...");
        eliminarVenta(0, 0);
        mostrarVentas();

        sc.close();
    }
}

