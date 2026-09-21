async function checkBackend() {

    const result = document.getElementById("result");

    result.innerText = "Checking backend...";

    try {

        const response = await fetch("/api/health");

        const data = await response.text();

        result.innerText = "Backend response: " + data;

    } catch (error) {

        result.innerText = "Backend connection failed";

        console.error(error);
    }
}