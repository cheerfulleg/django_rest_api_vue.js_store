export default function toFixed(value) {
    value = parseFloat(value);
    return '$' + value.toFixed(2)
}
