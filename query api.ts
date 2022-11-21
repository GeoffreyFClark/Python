// Implementation code where T is the returned data shape
function api<T>(url: string): Promise<T> {
	return fetch(url).then((response) => {
		if (!response.ok) {
			throw new Error(response.statusText);
		}
		return response.json() as Promise<T>;
	});
}

// For "unwrapping" e.g. top level attribute

function api<T>(url: string): Promise<T> {
	return fetch(url)
		.then((response) => {
			if (!response.ok) {
				throw new Error(response.statusText);
			}
			return response.json() as Promise<{ data: T }>;
		})
		.then((data) => {
			return data.data;
		});
}
