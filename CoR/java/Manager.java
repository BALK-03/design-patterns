public class Manager extends Approver {
    private final double APPROVAL_LIMIT = 5000.0;

    @Override
    public void processRequest(PurchaseRequest request) {
        if (request.getAmount() <= APPROVAL_LIMIT) {
            System.out.println("Manager approved purchase request #" + request.getRequestNumber());
        } else if (nextApprover != null) {
            nextApprover.processRequest(request);
        }
    }
}