package VehicleProject;

public class SecondHandVehicleTester {
    public static void main(String[] args) {
        System.out.print("Enter register number: ");
        String regNo = EasyScanner.nextString();
        System.out.print("Enter vehicle brand: ");
        String make = EasyScanner.nextString();
        System.out.print("Enter year of manufacture: ");
        int yearOfManufacture = EasyScanner.nextInt();
        System.out.print("Enter value: ");
        double value = EasyScanner.nextDouble();
        System.out.print("Enter number of owners: ");
        int numberOfOwners = EasyScanner.nextInt();

        SecondHandVehicle newCar = new SecondHandVehicle(regNo, make, yearOfManufacture, value, numberOfOwners);

        System.out.println("The car is " + newCar.calculateAge(2020) + " years old.");
        if(newCar.hasMultipleOwners()){
            System.out.println("Multiple owners.");
        } else {
            System.out.println("Only owner");
        }
    }
}
