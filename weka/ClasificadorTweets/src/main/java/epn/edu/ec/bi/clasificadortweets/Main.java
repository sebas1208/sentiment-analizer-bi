/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package epn.edu.ec.bi.clasificadortweets;

/**
 *
 * @author sebastian
 */
public class Main {
        /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception {
        // TODO code application logic here
        RedNeuronal net = new RedNeuronal();
        net.training("-L 0.3 -M 0.2 -N 1000 -V 0 -S 0 -E 20 -H 5 -R");
        net.validate();
        //net.testing();
    }
}
