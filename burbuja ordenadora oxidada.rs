/* fn main() {
  let ls = [3,5,8,6,5,9,2,3,5];
  let mut zz;
  for i in ls {
   for j in ls -(i - 1){
   if ls[j] > ls[j+1]{
            zz=ls[j];
            ls[j]=ls[j+1];
            ls[j+1]=zz;
   }
   println!("{:?}", ls);
  }
    
  }
}
*/
fn main() {
    let mut ls = [3,5,8,6,5,9,2,3,5];       //establece la lista, los cambios se realizaran en esta misma
    let zz = ls.len();                      //cuenta la cantidad de numeros en la lista
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 0..zz - 1 {                //para i dentro de la lista
            if ls[i] > ls[i + 1] {          //si el numero actual es mayor que el anterior...
                ls.swap(i, i + 1);          //el numero actual ocupara la posicion de adelante
                swapped = true;
            }
           println!("{:?}", ls);            //imprime la lista corregida
        }
    }
}