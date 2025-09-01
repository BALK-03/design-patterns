public class Client {
    public static void main(String[] args) {
        CarDirector dir = new CarDirector();

        // Build a sports car
        SportsCarBuilder sportsCarBuilder = new SportsCarBuilder();
        dir.constructCar(sportsCarBuilder);

        Car sportCar = sportsCarBuilder.build();
        System.out.println(sportCar);
    }
}