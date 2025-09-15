// src/entries/app.js
import '../stylesheets/app.css';
import App from '../layouts/App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;