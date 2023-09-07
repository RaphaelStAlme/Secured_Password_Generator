export default abstract class PasswordService {
    static async generatePassword(digits: boolean, symbols: boolean, length: string | null, hash: boolean) {
        console.log(length);
        var response = await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${length}&hash=${hash}`);
        return response.json();
    }
}

