// inherit

class Calculate{
  int add(int a, int b){
    return a+b;
  }
}
class Calculate2 extends Calculate{
  // functions
  int subtract(int a, int b){
    return a-b;
  }
}
int main()
{
  // Decisicion making

  int a = 1;
  if(a == 1){
    print("A is one");
  }

  // looping

  for(int i = 0; i < 10; i++){
    print(i);
  }

  // inheritance
  Calculate2 c = Calculate2();
  print(c.add(10,20));
  print(c.subtract(10, 20));
  return 0;
}


