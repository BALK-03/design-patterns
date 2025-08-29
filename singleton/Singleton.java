public  class Singleton {
    // volatile makes sure no partially constructed object is called, till its full initialized
    private static volatile Singleton instance;
    private String data;

    private Singleton(String data) {
        this.data = data;
    }

    public static Singleton getInstance(String data) {
        Singleton result = instance; // A read from volatile  slightly slower thats why we fetche one, use everywhrere
        if (result == null) { // Solving the over-head problem (even if the instance was created, every thread has to wait before returning it)           // Makes sure the multi-thread problem is solved
            synchronized (Singleton.class) {
                result = instance;
                if (result == null) {
                    instance = result = new Singleton(data);
                }
            }
        }
        return instance;
    }
}