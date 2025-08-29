public abstract class Application {
    public Document OpenDocument() {
        Document doc = createDocument();
        doc.open();
        return doc;
    }

    public abstract Document createDocument();
}