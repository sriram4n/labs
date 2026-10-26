void main(){
  int x = 10;
  double y = 10.3;
  bool z = false;
  String a = "amongus";
  // datatype is flexible
  dynamic b = "Hello";
  print(b);
  b = 3.14;
  print(b);
  print(x);
  print(y);
  print(z);
  print(a);

// changes cant be made
  final String final_string  = "IM FINAL";
  print(final_string);

// no datatype
  const constant_var = "im constant";
  print(constant_var);
  int? im_null; //declare without initialization
  im_null = null;
  print(im_null);
 
}