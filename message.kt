import java.io.IOException

fun main() {
    val phoneNumber = "+233202334725" // Replace with the recipient's phone number (including the country code)

    val message = "Happy Birthday!"

    try {
        val process = Runtime.getRuntime().exec("cmd /c start https://wa.me/$phoneNumber/?text=$message")
        process.waitFor()
    } catch (e: IOException) {
        e.printStackTrace()
    } catch (e: InterruptedException) {
        e.printStackTrace()
    }
}
