public class Car {
    private String engine;
    private String tires;
    private String color;

    public void setEngine(String engine) {
        this.engine = engine;
    }

    public void setTires(String tires) {
        this.tires = tires;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return "Car: Engine=" + engine + ", Tires=" + tires + ", Color=" + color;
    }
}