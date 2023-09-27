function reverseString(inputString) {
    let reversed = '';
    for (let i = inputString.length - 1; i >= 0; i--) {
      reversed += inputString[i];
    }
    return reversed;
  }
  
  const input = "ANA MOSH ANA";
  const reversed = reverseString(input);
  
  console.log(reversed);
  