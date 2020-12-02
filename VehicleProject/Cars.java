package VehicleProject;

import java.util.ArrayList;

public class Cars
{
    ArrayList<SecondHandVehicle> newVehicle = new ArrayList<>();

    private int search(String regNoIn){
        for(int i=0; i<newVehicle.size(); i++){
            SecondHandVehicle tempVehicle = newVehicle.get(i);
            String tempRegNo = tempVehicle.getRegNo();
            if(tempRegNo.equals(regNoIn)){
                return i;
            }
        }
        return -999;
    }
    
    public boolean addVehicle(String regNo){
        if(search(regNo) == -999){
            System.out.print("Enter vehicle brand: ");
            String make = EasyScanner.nextString();
            System.out.print("Enter year of manufacture: ");
            int yearOfManufacture = EasyScanner.nextInt();
            System.out.print("Enter value: ");
            double value = EasyScanner.nextDouble();
            System.out.print("Enter number of owners: ");
            int numberOfOwners = EasyScanner.nextInt();
        
            newVehicle.add(new SecondHandVehicle(regNo, make, yearOfManufacture, value, numberOfOwners));

            return true;
        }
        return false;        
    }

    public void displayVehicles(){
        for(int i=0; i<newVehicle.size(); i++){
            System.out.println();
            System.out.println("Vehicle # " + (i+1));
            System.out.println("Register Number: " + newVehicle.get(i).getRegNo());
            System.out.println("Brand: " + newVehicle.get(i).getMake());
            System.out.println("Year of manufacture: " + newVehicle.get(i).getYearOfManufacture());
            System.out.println("The car is " + newVehicle.get(i).calculateAge(2020) + " years old.");
            if(newVehicle.get(i).hasMultipleOwners()){
                System.out.println("Multiple owners.");
            } else {
                System.out.println("Only owner");
            }
            System.out.println();
        }
    }

    public boolean deleteVehicle(String regNoIn){
        int index = search(regNoIn);
        if(index != -999){
            newVehicle.remove(index);
            return true;
        } else {
            return false;
        }
    }
}