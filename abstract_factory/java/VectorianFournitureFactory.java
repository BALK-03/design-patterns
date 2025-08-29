public class VectorianFournitureFactory extends FournitureFactory {
    @Override
    public Chair createChair() {
        return new VectorianChair();
    }

    @Override
    public Sofa createSofa() {
        return new VectorianSofa();
    }
}