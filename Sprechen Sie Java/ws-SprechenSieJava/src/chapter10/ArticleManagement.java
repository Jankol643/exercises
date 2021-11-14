package chapter10;

import java.io.IOException;
import java.util.ArrayList;
import java.io.FileInputStream;
import java.util.Scanner;

class Article {
    int id;
    float singlePrice;
    int[] quantity;
}

class ArticleManagement {
    public static ArrayList<Article> articleList = new ArrayList<Article>();

    public static void main(String[] args) {
        readSalesData();
        printSalesData();
    }

    public static void readSalesData() {
        // read first line of file
        String filename = "10_SalesData.txt";
        filename = "resources/" + filename;
        ArrayList<String> lines = new ArrayList<String>();

        try {
            // the file to be opened for reading
            FileInputStream fis = new FileInputStream(filename);
            Scanner sc = new Scanner(fis); // file to be scanned
            // returns true if there is another line to read
            while (sc.hasNextLine()) {
                lines.add(sc.nextLine());
            }
            sc.close(); // closes the scanner
        } catch (IOException e) {
            e.printStackTrace();
        }

        for (int i = 0; i < lines.size(); i++) {
            readArticle(lines.get(i));
        }

    }

    public static void printSalesData() {
        int noArticles = articleList.size();
        System.out.println("Article no." + "\t" + "turnover");
        for (int i = 0; i <= noArticles; i++) {
            Article a = articleList.get(i);
            printArticle(a);
        }
    }

    public static Article readArticle(String line) {
        String[] splitted = line.split("\t");
        Scanner sc = new Scanner(line).useDelimiter("\t");
        int id = sc.nextInt();
        float singlePrice = sc.nextFloat();
        // Read amounts of articles

        Article a = new Article(id, singlePrice, quantity);
        articleList.add(a);
    }

    public static void printArticle(Article a) {
        int articleNo = a.id;
        int quantitySum = 0;
        for (int i = 0; i < a.quantity.length; i++) { // loop through quantities
            int quant = a.quantity[i];
            quantitySum += quant;
        }
        float turnover = quantitySum * a.singlePrice;

        System.out.println(articleNo + "\t" + turnover);
    }
}