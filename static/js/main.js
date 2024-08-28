function copyToClipboard(id) {
    const textField = document.getElementById(id).shadowRoot.querySelector('input');
    textField.select();
    document.execCommand("copy");
    alert("Copied the text: " + textField.value);
}
