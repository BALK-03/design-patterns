public class Client {
    public static void main(String[] args) {
        // Modern Factory
        FournitureFactory modernFactory = new ModernFournitureFactory();
        Chair modernChair = modernFactory.createChair();
        modernChair.businessLogic();

        Sofa modernSofa = modernFactory.createSofa();
        modernSofa.businessLogic();
    }
}