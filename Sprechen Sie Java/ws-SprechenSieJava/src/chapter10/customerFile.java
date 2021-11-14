package chapter10;
import java.io.File;
import java.util.Scanner;

class Client {
    int id;
    String name;
    Address priv;
    Address office;
    Order[] orderList;
}

class Address {
    String street;
    int houseNo;
    int zipCode;
    String city;
}

class Order {
    int amount; // number of articles ordered
    int articleId;
    int articlePrice;
}

class customerFile {
    static Client[] client; // client "database"
    static int noClients; // number of clients

    static void readClientFile() {
        String filename = "10_customerData.txt";
        filename = "resources/" + filename;

        client = new Client[1000];
        try {
            File file = new File(filename);
            Scanner sc = new Scanner(file); // file to be scanned
            while (sc.hasNextLine()) // returns true if and only if scanner has another token
                System.out.println(sc.nextLine());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void readClient() {

    }

    static Address readAddress() {

        return new Address(street, houseNo, zipCode, city);
    }

}
