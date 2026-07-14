function analyzeSentiment() {

    let text =
        document.getElementById("textInput").value;

    let loading =
        document.getElementById("loading");

    let sentiment =
        document.getElementById("sentiment");

    let confidence =
        document.getElementById("confidence");

    loading.innerHTML = "AI is analyzing...";

    setTimeout(() => {

        if (text.length === 0) {
            sentiment.innerHTML =
                "Please enter some text.";
            confidence.innerHTML = "--";
        }

        else if (
            text.includes("love") ||
            text.includes("happy") ||
            text.includes("great")
        ) {
            sentiment.innerHTML = "Positive 😊";
            confidence.innerHTML = "95%";
        }

        else if (
            text.includes("hate") ||
            text.includes("bad") ||
            text.includes("terrible")
        ) {
            sentiment.innerHTML = "Negative ☹️";
            confidence.innerHTML = "93%";
        }

        else {
            sentiment.innerHTML = "Neutral 😐";
            confidence.innerHTML = "90%";
        }

        loading.innerHTML = "";

    }, 2000);
}
