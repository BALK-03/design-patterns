public class CEO extends Approver {
    @Override
    public void processRequest(PurchaseRequest request) {
        System.out.println("CEO approved purchase request #" + request.getRequestNumber());
    }
}