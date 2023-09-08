export default abstract class PasswordService {
    /**
 * Generate a password using the API.
 * @param digits - Whether to include digits in the password.
 * @param symbols - Whether to include symbols in the password.
 * @param passwordLength - The desired length of the password (default is 8 if not defined).
 * @param hash - Whether to hash the generated password.
 * @returns A Promise that resolves to the generated password.
 */
    // Method which call API in order to generate a password
    static async generatePassword(digits: boolean, symbols: boolean, passwordLength: string, hash: boolean) {
        var response = await fetch(`http://127.0.0.1:5000/generate_password?digits=${digits}&symbols=${symbols}&length=${passwordLength}&hash=${hash}`);
        return response.json();
    }
}

