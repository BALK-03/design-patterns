public class Director extends Approver {
    private final double APPROVAL_LIMIT = 20000.0;

    @Override
    public void processRequest(PurchaseRequest request) {
        if (request.getAmount() <= APPROVAL_LIMIT) {
            System.out.println("Director approved purchase request #" + request.getRequestNumber());
        } else if (nextApprover != null) {
            nextApprover.processRequest(request);
        }
    }
}