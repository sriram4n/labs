class Add {
  int add(int a, int b) {
    return a + b;
  }
}

class Multiply extends Add {
  int multiply(int a, int b) {
    return a * b;
  }
}

void main() {
  Multiply m = Multiply();
  print(m.add(10, 20));
  print(m.multiply(10, 20));
}
