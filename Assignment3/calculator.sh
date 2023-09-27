#!/bin/bash

#addition
add() {
    echo "Result: $(($1 + $2))"
}

#subtraction
subtract() {
    echo "Result: $(($1 - $2))"
}

#multiplication
multiply() {
    echo "Result: $(($1 * $2))"
}

#division
divide() {
    if [ $2 -ne 0 ]; then
        result=$(echo "scale=2; $1 / $2" | bc)
        echo "Result: $result"
    else
        echo "Division by zero is not allowed."
    fi
}

# Main calculator loop
while true; do
    echo "Select operation:"
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    echo "5. Quit"
    read choice

    case $choice in
        1)  echo "Enter two numbers:"
            read num1
            read num2
            add $num1 $num2
            ;;
        2)  echo "Enter two numbers:"
            read num1
            read num2
            subtract $num1 $num2
            ;;
        3)  echo "Enter two numbers:"
            read num1
            read num2
            multiply $num1 $num2
            ;;
        4)  echo "Enter two numbers:"
            read num1
            read num2
            divide $num1 $num2
            ;;
        5)  echo "Exiting calculator."
            exit 0
            ;;
        *)  echo "Invalid choice. Please select a valid option."
            ;;
    esac

    echo "-------------------------------------"
done
