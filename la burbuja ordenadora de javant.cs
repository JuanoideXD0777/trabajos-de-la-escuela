using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
    int[] arr = { 3, 5, 8, 6, 5, 9, 2, 3, 5};       //es la lista
    int n = arr.Length;                             //mide la cantidad de numeros dentro del arreglo
    bool swapped;                                   //establece un tope para el loop
          
      foreach (int i in arr)                        //imprime la lista
      {
      Console.WriteLine(i);
      }
      Console.WriteLine("\n\n");
    do
    {
        swapped = false;
        for (int i = 0; i < n - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                // Intercambiar arr[i] y arr[i+1]
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
                      
      foreach (int j in arr)
      {
      Console.WriteLine(j);
      }
      Console.WriteLine("\n");
            }
        }
      } while (swapped);
    }
  }
}