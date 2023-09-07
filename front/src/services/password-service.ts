export default abstract class PasswordService {
    static async generatePassword(digits: boolean, symbols: boolean, passwordLength: string, hash: boolean) {
        var response = await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${passwordLength}&hash=${hash}`);
        return response.json();
    }
}

