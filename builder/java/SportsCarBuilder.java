public class SportsCarBuilder implements CarBuilder {
    private Car car;

    public SportsCarBuilder() {
        this.car = new Car();
    }

    @Override
    public void setEngine() {
        car.setEngine("V8 Turbo");
    }

    @Override
    public void setTires() {
        car.setTires("Performance Tires");
    }

    @Override
    public void setColor() {
        car.setColor("Red");
    }

    @Override
    public Car build() {
        return this.car;
    }
}