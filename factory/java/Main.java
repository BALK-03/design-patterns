public class Main {
    public static void main(String[] args) {
        Application textApp = new TextApplication();
        Document textDoc = textApp.OpenDocument();

        System.out.println();

        Application richTextApp = new RichTextApplication();
        Document richTextDoc = richTextApp.OpenDocument();
    }
}