export default abstract class PasswordService {
    static async generatePassword(digits: string | null, symbols: string | null, length: string | null) {
        console.log(length);
        var response = await fetch(`http://127.0.0.1:5000/generate_password?length=${length}`);
        return response.json();
    }
}

