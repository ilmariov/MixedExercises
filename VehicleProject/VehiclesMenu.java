package VehicleProject;

public class VehiclesMenu {
    public static void main(String[] args) {
        char choice;
        Cars myCar = new Cars();
        do
        {
            System.out.println("1. Add a Vehicle");
            System.out.println("2. Display a list of vehicle details");
            System.out.println("3. Delete a vehicle");
            System.out.println("4. Quit");

            System.out.print("Choose among the options above: ");
            choice = EasyScanner.nextChar();

            switch (choice){
                case '1': option1(myCar);
                        break;
                case '2': option2(myCar);
                        break;
                case '3': option3(myCar);
                        break;
                case '4': System.out.println("Good Bye");
                        break;
            }
        } while (choice != '4');
    }

    static void option1(Cars carIn) {
        System.out.print("Enter register number: ");
        String regNo = EasyScanner.nextString();

        boolean entered = carIn.addVehicle(regNo);
        if (entered) {
            System.out.println("Vehicle added.");
        } else {
            System.out.println("Vehicle already exists.");
        }
    }

    public static void option2(Cars carIn) {
        carIn.displayVehicles();
    }

    static void option3(Cars carIn){
        System.out.print("Enter register number of the car to be removed: ");
        String regNo = EasyScanner.nextString();
        boolean removed = carIn.deleteVehicle(regNo);
        if(removed){
            System.out.println("The vehicle was succesfuly removed.");
        } else {
            System.out.println("No such vehicle.");
        }
    }
}
