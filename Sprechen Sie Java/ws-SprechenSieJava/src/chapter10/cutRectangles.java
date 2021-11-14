package chapter10;

class Rectangle {
    int x, y; // left top corner
    int width; // width of rectangle
    int height; // height of rectangle
}

class cutRectangles {

    public static void main(String[] args) {

    }

    private static Rectangle intersection(Rectangle r1, Rectangle r2) {
        int xmin = Math.max(r1.x, r2.x);
        int xmax1 = r1.x + r1.width;
        int xmax2 = r2.x + r2.width;
        int xmax = Math.min(xmax1, xmax2);
        if (xmax > xmin) {
            int ymin = Math.max(r1.y, r2.y);
            int ymax1 = r1.y + r1.height;
            int ymax2 = r2.y + r2.height;
            int ymax = Math.min(ymax1, ymax2);
            if (ymax > ymin) {
                int x = xmin;
                int y = ymin;
                int width = xmax - xmin;
                int height = ymax - ymin;
                return new Rectangle(x, y, width, height);
            }
        }
        return null;
    }
}