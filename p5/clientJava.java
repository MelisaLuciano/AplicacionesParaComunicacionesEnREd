import org.apache.xmlrpc.*; 
  
public class clienteJava{ 
  
public static void main (String [] args) { 
 try { 
  
      System.out.println("Iniciando el servidor XML-RPC..."); 
        
      WebServer server = new WebServer(80); 
      OperacionMatematica op = new OperacionMatematica(); 
      server.addHandler("miServidor", op); 
        
      server.start(); 
        
      System.out.println("Inicio exitoso del Servidor, queda en espera de peticiones del cliente..."); 
             System.out.println("se conecto"); 
        
    } catch (Exception exception) { 
      System.err.println("Server: " + exception); 
    } 
  } 
} 